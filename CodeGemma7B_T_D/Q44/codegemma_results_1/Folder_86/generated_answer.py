def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(43, 87):
        if 1 < nums[i] <= max(nums):
            composite_nums.add(nums[i])
    return composite_nums