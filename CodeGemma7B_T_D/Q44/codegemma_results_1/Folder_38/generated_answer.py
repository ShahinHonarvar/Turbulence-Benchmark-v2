def composite_nums_between_indices(nums):
    composites = set()
    for i in range(29, 94):
        if nums[i] % 1 == 0 and nums[i] % nums[i] == 0 and (nums[i] != 1):
            composites.add(nums[i])
    return composites