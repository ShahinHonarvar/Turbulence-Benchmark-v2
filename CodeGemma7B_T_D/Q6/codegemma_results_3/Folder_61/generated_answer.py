def all_neg_ints_exclusive(int_list):
    """Return a list of all negative integers from index 0 to index 7, both exclusive."""
    return [item for item in int_list if item < 0 and 0 <= item <= 7]