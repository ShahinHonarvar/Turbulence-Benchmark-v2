def composite_nums_between_indices(nums):
    if len(nums) < 31:
        return set()
    return {num for num in nums[30:31] if num > 1 and (not any((num % i == 0 for i in range(2, num))))}