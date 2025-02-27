def composite_nums_between_indices(nums):
    composite_nums = {num for num in nums[262:747] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_nums