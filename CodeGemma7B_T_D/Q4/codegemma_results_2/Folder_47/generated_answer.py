def all_pos_ints_exclusive(nums):
    """
    Returns a list of all positive integers from index 64 to index 80, both exclusive.
    If no positive integers exist in the specified range, the function returns an empty list.
    """
    return [num for num in nums if num > 0 and 64 < num < 80]