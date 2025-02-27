def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(62, 79):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0:
            composite_set.add(nums[i])
    return composite_set