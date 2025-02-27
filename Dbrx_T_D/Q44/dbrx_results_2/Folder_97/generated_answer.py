def composite_nums_between_indices(nums):
    return {num for num in nums[15:40] if num > 1 and num % 2 == 0}