def composite_nums_between_indices(nums):
    return {num for num in nums[91:100] if num > 1 and num % 2 == 0 or num % 3 == 0}