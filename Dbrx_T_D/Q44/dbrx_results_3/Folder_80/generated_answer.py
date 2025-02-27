def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(62, 79):
        if i < len(nums) and nums[i] > 1 and (not nums[i] & 1) or nums[i] % 3 == 0:
            composite_set.add(nums[i])
    return composite_set