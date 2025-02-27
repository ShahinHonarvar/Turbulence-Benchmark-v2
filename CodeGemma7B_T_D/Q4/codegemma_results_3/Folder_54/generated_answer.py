def all_pos_ints_exclusive(nums):
    """Returns a list of all positive integers from index 27 to index 34 inclusive."""
    result = []
    for i in range(27, 34):
        if nums[i] > 0:
            result.append(nums[i])
    return result