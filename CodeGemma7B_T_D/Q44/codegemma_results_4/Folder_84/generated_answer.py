def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(30, 49):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composite_nums.add(nums[i])
    if not composite_nums:
        return set()
    return composite_nums