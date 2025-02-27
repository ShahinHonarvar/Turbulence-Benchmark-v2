def composite_nums_between_indices(nums):
    composites_set = set()
    for idx in range(22, 51):
        if nums[idx] % 2 == 0 or nums[idx] % 3 == 0:
            composites_set.add(nums[idx])
    if len(composites_set) == 0:
        return set()
    return composites_set