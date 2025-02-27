def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(667, 775):
        if nums[i] in composite_nums:
            continue
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums