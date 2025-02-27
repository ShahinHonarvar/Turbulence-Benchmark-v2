def composite_nums_between_indices(nums):
    composites = set()
    for i in range(74, 96):
        if i < len(nums):
            if nums[i] % 2 == 0 or nums[i] % 3 == 0:
                composites.add(nums[i])
    return composites