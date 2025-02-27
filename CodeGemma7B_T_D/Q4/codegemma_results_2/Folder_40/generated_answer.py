def all_pos_ints_exclusive(nums):
    """Return list of all positive ints at indices 0 to 2 (exclusive)."""
    result = []
    for i in range(3):
        if i > 0 and nums[i] > 0:
            result.append(nums[i])
    return result