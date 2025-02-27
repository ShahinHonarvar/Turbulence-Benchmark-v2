def composite_nums_between_indices(nums):
    composites = set()
    for i in range(22, 64):
        if nums[i] % 2 == 0:
            composites.add(nums[i])
        for j in range(3, int(nums[i] ** 0.5) + 1, 2):
            if nums[i] % j == 0:
                composites.add(nums[i])
    return composites or set()