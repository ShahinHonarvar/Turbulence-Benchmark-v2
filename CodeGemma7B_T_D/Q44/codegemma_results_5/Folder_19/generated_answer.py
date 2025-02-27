def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(5, 8):
        if nums[i] != 1 and nums[i] not in prime_nums:
            composite_nums.add(nums[i])
    if not composite_nums:
        return set()
    return composite_nums