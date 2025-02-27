def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(50, 201):
        if nums[i] != 1 and any((num <= nums[i] and nums[i] % num == 0 for num in range(2, int(nums[i] ** 0.5) + 1))):
            composite_nums.add(nums[i])
    return composite_nums