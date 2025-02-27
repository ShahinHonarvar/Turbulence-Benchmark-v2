def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(62, 100):
        if nums[i] > 1 and all((i % j != 0 for j in range(2, int(nums[i] ** 0.5) + 1))):
            composite_set.add(nums[i])
    return composite_set