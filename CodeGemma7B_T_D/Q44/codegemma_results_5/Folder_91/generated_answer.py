def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(5, 6):
        if 1 < nums[i] < nums[i + 1]:
            composite_set.add(nums[i])
    if not composite_set:
        return set()
    return composite_set