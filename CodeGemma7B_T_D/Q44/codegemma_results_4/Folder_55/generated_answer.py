def composite_nums_between_indices(nums):
    composites = set()
    for i in range(10, 101):
        if nums[i] % 2 != 0 and nums[i] % 3 != 0 and (nums[i] % 5 != 0) and (nums[i] % 7 != 0):
            composites.add(nums[i])
    return composites