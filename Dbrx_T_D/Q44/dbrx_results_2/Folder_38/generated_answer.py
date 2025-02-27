def composite_nums_between_indices(nums):
    composite_set = set(filter(lambda x: x > 1 and x % 2 == 0 or x % 3 == 0, nums[29:94]))
    return composite_set