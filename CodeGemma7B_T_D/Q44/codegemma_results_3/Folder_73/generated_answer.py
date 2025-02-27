def composite_nums_between_indices(nums):
    composites = set()
    for i in range(28, 41):
        if 28 <= i < len(nums) and nums[i] != 1 and (not is_prime(nums[i])):
            composites.add(nums[i])
    return composites