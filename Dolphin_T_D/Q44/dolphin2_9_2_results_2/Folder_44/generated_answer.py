def composite_nums_between_indices(nums):
    composites = set()
    for i in range(64, 67):
        if all((i % n != 0 for n in range(2, i))):
            continue
        if nums[i] > 1:
            composites.add(nums[i])
    return composites