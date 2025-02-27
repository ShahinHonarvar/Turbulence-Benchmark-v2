def composite_nums_between_indices(nums):
    return set(nums[30:87]) & set(range(2, int(nums[30] ** 0.5) + 1))