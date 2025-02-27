def composite_nums_between_indices(nums):
    composites = set()
    for i in range(91, 100):
        if 1 < nums[i] <= 4:
            composites.add(nums[i])
    return composites