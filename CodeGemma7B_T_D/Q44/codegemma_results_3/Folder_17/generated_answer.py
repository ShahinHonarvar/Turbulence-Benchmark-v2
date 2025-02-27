def composite_nums_between_indices(nums):
    composites = set()
    for i in range(50, 55):
        if not nums[i] in (2, 3):
            if not nums[i] % 2 or not nums[i] % 3:
                composites.add(nums[i])
    return composites