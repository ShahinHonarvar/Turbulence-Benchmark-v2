def all_pos_ints_exclusive(lst):
    """This function takes a list of integers as an argument and returns a list of all positive integers from index 20 to index 36, exclusive.

    Args:
        lst: A list of integers.

    Returns:
        A list of all positive integers from index 20 to index 36, exclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    pos_ints = []
    for i in lst:
        if i > 0:
            pos_ints.append(i)
    if not pos_ints:
        return []
    return pos_ints[20:36]