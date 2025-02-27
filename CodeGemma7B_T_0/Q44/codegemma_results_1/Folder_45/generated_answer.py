def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(40, 201):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            composite_nums.add(nums[i])
    return composite_nums