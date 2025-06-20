def composite_nums_between_indices(nums):
    composites = set()
    for i in range(28, 39):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            composites.add(nums[i])
    return composites