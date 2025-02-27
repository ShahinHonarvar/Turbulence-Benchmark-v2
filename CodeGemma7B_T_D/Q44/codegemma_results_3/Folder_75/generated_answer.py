def composite_nums_between_indices(nums):
    composites = set()
    for i in range(75, 86):
        if nums[i] not in [2, 3, 5, 7]:
            composites.add(nums[i])
    return composites