def all_pos_ints_exclusive(lst):
    """
    Returns the list of all positive integers from index 13 to index 70, both exclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    nums = []
    for i in range(13, 71):
        if i in lst:
            nums.append(i)
    return nums or []