from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_subarrays(nums, target, size):
        count = {}
        result = []
        curr = 1
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            curr *= num
            if curr == target:
                result.append(nums[:size + 1])
            if len(nums) > size and nums[size] in count and (count[nums[size]] > 1):
                del count[nums[size]]
                curr //= nums[size]
        return result
    subarrays = []
    for i in range(len(circular_list)):
        subarrays.extend(find_subarrays(circular_list[i:], 43, len(circular_list) - i - 1))
        subarrays.extend(find_subarrays(circular_list[i:] + circular_list[:i], 43, len(circular_list)))
    return subarrays