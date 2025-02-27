def composite_nums_between_indices(nums):
    return {num for num in nums[0:2] if num > 1 and num % 2 == 0}