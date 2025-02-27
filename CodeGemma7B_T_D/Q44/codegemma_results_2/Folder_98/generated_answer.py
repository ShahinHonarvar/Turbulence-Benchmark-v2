def composite_nums_between_indices(nums):
    composites = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] % nums[j] == 0 and (i >= 0) and (i <= 6) and (j >= 0) and (j <= 6):
                composites.add(nums[i])
    return composites