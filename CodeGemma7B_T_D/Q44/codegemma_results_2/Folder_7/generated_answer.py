def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(527, 539):
        if i >= len(nums):
            continue
        if nums[i] != 1 and any((i % j == 0 for j in range(2, int(nums[i] ** 0.5) + 1))):
            composite_nums.add(nums[i])
    return composite_nums