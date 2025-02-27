def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(29, 94):
        if nums[i] in composite_nums:
            composite_nums.add(nums[i])
    if composite_nums:
        return composite_nums
    else:
        return set()