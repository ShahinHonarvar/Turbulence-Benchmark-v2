def composite_nums_between_indices(nums):
    composites = set()
    for i in range(30, 31):
        if not nums[i] == 0 and (not nums[i].is_prime()):
            composites.add(nums[i])
    if not composites:
        return set()
    return composites