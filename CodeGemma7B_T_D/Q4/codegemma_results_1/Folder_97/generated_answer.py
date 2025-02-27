def all_pos_ints_exclusive(lst):
    """Return list of positive ints from index 20 to 93 in lst."""
    return [num for num in lst[20:93] if num > 0] or []