def all_neg_ints_inclusive(nums):
    """Return a list of all negative integers from index 68 to index 86, inclusive.
    If no negative integers exist in the specified range, return an empty list."""
    result = []
    for i in range(68, 87):
        if nums[i] < 0:
            result.append(nums[i])
    return result