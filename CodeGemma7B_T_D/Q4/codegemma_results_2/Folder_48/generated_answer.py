def all_pos_ints_exclusive(lst):
    """
    Returns a list of all positive integers from index 385 to index 999, both exclusive.
    """
    positive_ints = [i for i in lst[385:999] if i > 0]
    return positive_ints if positive_ints else []