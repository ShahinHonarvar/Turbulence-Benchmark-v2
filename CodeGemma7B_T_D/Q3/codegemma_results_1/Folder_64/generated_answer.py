def all_pos_ints_inclusive(lst):
    """
    Returns all positive integers from index 0 to index 4, inclusive.
    """
    return [lst[i] for i in range(len(lst)) if lst[i] > 0 and i >= 0 and (i <= 4)]