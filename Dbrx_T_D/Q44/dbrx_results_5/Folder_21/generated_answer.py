def composite_nums_between_indices(nums):
    return {num for num in nums[262:747] if num > 1 and num % 2 == 0}