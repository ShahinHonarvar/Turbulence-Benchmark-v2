def composite_nums_between_indices(nums):
    composites = set()
    for i in range(70, 85):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0:
            composites.add(nums[i])
    return composites if composites else set()