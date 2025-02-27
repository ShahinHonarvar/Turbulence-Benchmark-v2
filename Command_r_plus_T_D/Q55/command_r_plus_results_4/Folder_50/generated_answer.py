from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:

    def product(nums: List[int]) -> int:
        result = 1
        for num in nums:
            result *= num
        return result

    def find_subarrays(nums: List[int], target_product: int) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j + 1]
                if product(subarray) == target_product:
                    result.append(subarray)
        return result
    return find_subarrays(nums, 45)