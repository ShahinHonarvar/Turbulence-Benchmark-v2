def all_ints_exclusive(lst):
    return [val for i, val in enumerate(lst) if i not in range(20, 36)]