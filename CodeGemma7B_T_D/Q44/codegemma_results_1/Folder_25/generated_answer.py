def composite_nums_between_indices(nums):
    composites = set()
    for i in range(75, 95):
        if is_composite(nums[i]):
            composites.add(nums[i])
    return composites