def composite_nums_between_indices(nums):
    composite_nums = {num for num in nums[23:30] if num > 1 and num % 2 == 0}
    return composite_nums