def all_odd_ints_exclusive(int_list):
    """
    Returns the list of all odd integers from index 0 to index 10, both exclusive.

    If no odd integers exist in the specified range, the function should return an empty list.
    """
    return [i for i in int_list[0:11] if i % 2 != 0]