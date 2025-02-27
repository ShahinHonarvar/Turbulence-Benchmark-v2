def all_odd_ints_exclusive(lst):
    return [val for i, val in enumerate(lst) if 41 < i < 69 and val % 2 != 0]