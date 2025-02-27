def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(min(5, len(nums)), max(0, min(5, len(nums)) - 1), -1):
        if nums[i] > 1 and nums[i] % 2 == 0:
            composite_nums.add(nums[i])
    return composite_nums