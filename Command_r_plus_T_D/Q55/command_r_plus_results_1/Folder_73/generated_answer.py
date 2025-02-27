def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(nums, target, size):
        count = {}
        curr_product = 1
        res = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            curr_product = curr_product * num
            if curr_product == target:
                res.append(list(count.keys()))
            while len(nums) >= size and curr_product * nums[size] == target:
                count[nums[size]] += 1
                res.append(list(count.keys()))
                size += 1
        return res
    subarrays = find_subarrays(circular_list, 40, 1)
    subarrays += find_subarrays(circular_list[::-1], 40, 1)
    return subarrays