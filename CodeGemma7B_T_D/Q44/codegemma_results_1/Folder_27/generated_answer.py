def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(22, 64):
        if 22 <= i <= 64 and nums[i] % 1 <= 1 and (nums[i] % 2 != 0):
            composite_nums.update({nums[i]})
    if not composite_nums:
        return set()
    return composite_nums