def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(12, 93):
        if nums[i] % 2 == 0 or (nums[i] % 3 == 0 and nums[i] != 3) or (nums[i] % 5 == 0 and nums[i] != 5):
            composite_nums.add(nums[i])
    return composite_nums