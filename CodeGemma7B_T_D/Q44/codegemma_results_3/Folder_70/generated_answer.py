def composite_nums_between_indices(nums):
    composite_nums = []
    for i in range(32, 36):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0:
            composite_nums.append(nums[i])
    return set(composite_nums)