def composite_nums_between_indices(nums):
    composites = set()
    for i in range(56, 58):
        if nums[i] > 1 and (not is_prime(nums[i])):
            composites.add(nums[i])
    return composites