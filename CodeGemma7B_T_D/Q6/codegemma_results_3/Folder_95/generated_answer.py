def all_neg_ints_exclusive(lst):
    """Returns the list of all negative integers from index 25 to index 80, both exclusive.
    If no negative integers exist in the specified range, the function should return an empty list."""
    return [num for num in lst[25:80] if num < 0]