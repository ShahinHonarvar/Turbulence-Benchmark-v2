def composite_nums_between_indices(nums):
    composites = set()
    for i in range(len(nums)):
        if i in range(0, i + 1):
            if not nums[i].isnumeric():
                composites.add(nums[i])
    return composites