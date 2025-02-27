def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(56, 58):
        if nums[i] not in [2, 3, 5, 7] and any((nums[i] % j == 0 for j in range(2, nums[i]))):
            composite_nums.add(nums[i])
    return composite_nums if composite_nums else set()