def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(56, 58):
        if not nums[i] % 2 or not nums[i] % 3:
            composite_nums.add(nums[i])
    return composite_nums