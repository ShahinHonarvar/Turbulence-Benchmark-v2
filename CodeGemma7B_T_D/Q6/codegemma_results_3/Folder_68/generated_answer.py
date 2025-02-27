def all_neg_ints_exclusive(lst):
    """
    Returns all negative integers from index 0 to index 8, both exclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(len(lst)):
        if lst[i] < 0 and i in range(9):
            result.append(lst[i])
    return result