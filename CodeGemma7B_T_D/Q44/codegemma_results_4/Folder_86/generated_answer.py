def composite_nums_between_indices(nums):
    composites = set()
    for i in range(43, 87):
        if nums[i] in (2, 3):
            continue
        is_composite = True
        for x in range(5, int(nums[i] ** 0.5) + 1, 2):
            if nums[i] % x == 0:
                composites.add(nums[i])
                is_composite = False
                break
        if is_composite:
            composites.add(nums[i])
    return composites or {}