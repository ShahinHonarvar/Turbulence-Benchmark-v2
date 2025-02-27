def all_pos_ints_exclusive(li):
    """
    The function takes one argument, a list of integers, and returns the list of all
    positive integers from index 0 to index 6, both exclusive. If no positive
    integers exist in the specified range, the function should return an empty list.
    """
    return [i for i in li if i > 0 and i < 7]