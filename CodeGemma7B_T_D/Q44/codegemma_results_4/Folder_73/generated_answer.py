def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(28, 41):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composite_nums.add(nums[i])
    return composite_nums or set()