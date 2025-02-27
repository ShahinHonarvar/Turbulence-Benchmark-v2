def all_odd_ints_exclusive(lst):
    return [val for i, val in enumerate(lst) if i > 295 and i < 573 and (val % 2 != 0)]