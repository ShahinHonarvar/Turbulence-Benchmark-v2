def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 389 to index 748, both exclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(389, 748):
        if nums[i] > 0:
            result.append(nums[i])
    return result