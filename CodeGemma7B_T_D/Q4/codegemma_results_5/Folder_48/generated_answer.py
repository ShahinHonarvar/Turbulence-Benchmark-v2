def all_pos_ints_exclusive(nums):
    """
    Returns a list of all positive integers from index 385 to index 999, both exclusive.

    Args:
      nums: A list of integers.

    Returns:
      A list of positive integers from index 385 to index 999, both exclusive. If no positive integers exist in the specified range, the function returns an empty list.
    """
    has_pos_ints = False
    for i in range(385, 1000):
        if nums[i] > 0:
            has_pos_ints = True
            break
    if not has_pos_ints:
        return []
    return nums[385:999]