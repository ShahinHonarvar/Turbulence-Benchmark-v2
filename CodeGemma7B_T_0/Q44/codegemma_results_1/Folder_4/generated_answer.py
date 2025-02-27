def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(56, 99):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            composite_set.add(nums[i])
    return composite_set