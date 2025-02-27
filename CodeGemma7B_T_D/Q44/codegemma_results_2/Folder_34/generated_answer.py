def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(70, 201):
        if nums[i] not in prime_nums:
            composite_nums.add(nums[i])
    return composite_nums