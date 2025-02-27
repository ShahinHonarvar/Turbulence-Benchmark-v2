def all_odd_ints_inclusive(lst):
    """
    Returns the list of all odd integers from index 75 to index 94, both inclusive.
    """
    return [num for num in lst[75:95] if num % 2 != 0] or []