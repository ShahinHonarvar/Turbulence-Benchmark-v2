def composite_nums_between_indices(nums):
    return {num for num in nums[75:89] if num > 1 and num % 2 == 0 or num % 3 == 0}