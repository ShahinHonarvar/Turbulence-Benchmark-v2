def all_pos_ints_exclusive(li):
    """
    Given a list of integers, return a list of all positive integers from index 11 to index 76, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    pos_ints = [i for i in li[11:76] if i > 0]
    return pos_ints