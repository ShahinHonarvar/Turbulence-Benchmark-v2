def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(14, 65):
        if nums[i - 1] % 2 != 0 and nums[i - 1] not in [4, 7]:
            composite_nums.add(nums[i - 1])
    return composite_nums