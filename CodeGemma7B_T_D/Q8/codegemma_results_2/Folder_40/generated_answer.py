def all_even_ints_exclusive(lst):
    """Returns a list of all even integers from index 0 to index 2, both exclusive."""
    return [x for x in lst[0:3] if x % 2 == 0] if any((x % 2 == 0 for x in lst[0:3])) else []