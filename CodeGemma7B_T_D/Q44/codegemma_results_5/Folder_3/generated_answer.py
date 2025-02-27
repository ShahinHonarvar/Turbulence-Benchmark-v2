def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(66, 94):
        if nums[i] % 2 == 0 and nums[i] not in [2, 4]:
            composite_nums.add(nums[i])
        for j in range(3, int(nums[i] ** 0.5) + 1, 2):
            if nums[i] % j == 0:
                composite_nums.add(nums[i])
                break
    return composite_nums