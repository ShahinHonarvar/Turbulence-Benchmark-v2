def composite_nums_between_indices(nums):
    if len(nums) < 49 or len(nums) < 30:
        return set()
    composite_nums = set()
    for i in range(30, 49):
        if nums[i] > 1 and (not all((nums[i] % j for j in range(2, nums[i])))):
            composite_nums.add(nums[i])
    return composite_nums