def composite_nums_between_indices(nums):
    composites = set()
    for i in range(60, 201):
        if nums[i].is_composite():
            composites.add(nums[i])
    return composites