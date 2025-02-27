def all_odd_ints_exclusive(lst):
    return [val for i, val in enumerate(lst[21:201], 21) if val % 2 != 0]