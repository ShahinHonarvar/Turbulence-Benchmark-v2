def composite_nums_between_indices(nums):
    composites = set()
    for i in range(62, 79):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or (i % 6 == 0 and i != 60):
            composites.add(nums[i])
    return composites