def composite_nums_between_indices(nums):
    return set((num for num in nums[62:93] if num > 1 and (not any((num % div == 0 for div in range(2, num)))))) if len(nums) >= 93 else set()