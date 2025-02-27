def all_pos_ints_exclusive(nums):
    """
    Returns a list of all positive integers from index 18 to index 37, both exclusive.

    Args:
        nums: A list of integers.

    Returns:
        A list of positive integers from index 18 to index 37, both exclusive. If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(18, 37):
        if nums[i] > 0:
            result.append(nums[i])
    return result