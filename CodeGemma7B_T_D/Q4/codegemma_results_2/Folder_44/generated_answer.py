def all_pos_ints_exclusive(lst):
    """
    Returns a list of all positive integers from index 81 to index 86, both exclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    result = [num for num in lst[80:86] if num > 0]
    return result if result else []