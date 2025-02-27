def composite_nums_between_indices(nums):
    """Returns a set of composite numbers in the given list that are between index 43 to index 51, both inclusive.

    If no composite number exists in the specified range, the function should return an empty set.
    """
    composite_nums = set()
    for i in range(43, 52):
        if nums[i] not in primes and nums[i] != 1:
            composite_nums.add(nums[i])
    return composite_nums