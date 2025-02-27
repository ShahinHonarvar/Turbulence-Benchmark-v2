def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(246, 751):
        if nums[i] not in [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]:
            composite_nums.add(nums[i])
    return composite_nums