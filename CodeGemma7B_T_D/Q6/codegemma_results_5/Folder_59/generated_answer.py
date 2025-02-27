def all_neg_ints_exclusive(lst):
    """
    Returns a list of all negative integers from index 0 to index 9, both exclusive.
    If no negative integers exist in the specified range, the function should
    return an empty list.
    """
    return [num for num in lst if num not in range(10) and num < 0]