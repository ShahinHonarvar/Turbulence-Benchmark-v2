def all_pos_ints_inclusive(nums):
    """
    Returns a list of all positive integers from index 36 to index 46, inclusive.
    """
    result = []
    for i in range(36, 47):
        if i >= 0:
            result.append(nums[i])
    return result