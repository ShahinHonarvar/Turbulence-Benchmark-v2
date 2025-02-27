def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(32, 36):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composite_set.add(nums[i])
    if composite_set:
        return composite_set
    else:
        return set()