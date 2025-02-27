def composite_nums_between_indices(nums):
    return {num for num in nums[686:988] if not num <= 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}