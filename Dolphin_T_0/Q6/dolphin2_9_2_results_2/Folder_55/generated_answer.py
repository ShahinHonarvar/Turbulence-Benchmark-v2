def all_neg_ints_exclusive(lst):
    """Returns a list of all negative integers from index 0 to index 10 (both exclusive). Returns an empty list if no negative integers exist in the specified range."""
    return [num for num in lst[2:10] if num < 0]