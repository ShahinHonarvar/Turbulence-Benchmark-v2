def composite_nums_between_indices(nums):
    composites = set()
    for i in range(37, 52):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composites.add(nums[i])
    return composites