def composite_nums_between_indices(nums):
    return {num for num in nums[29:52] if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0)}