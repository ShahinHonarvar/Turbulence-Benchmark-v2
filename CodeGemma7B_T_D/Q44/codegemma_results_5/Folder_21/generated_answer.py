def composite_nums_between_indices(nums):
    composites = set()
    for i in range(262, 747):
        if (nums[i] % 2 == 0 or nums[i] % 3 == 0) and nums[i] != 1 and (nums[i] != 2) and (nums[i] != 3):
            composites.add(nums[i])
    return composites