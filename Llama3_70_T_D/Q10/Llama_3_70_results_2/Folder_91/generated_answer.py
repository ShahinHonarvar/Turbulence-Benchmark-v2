def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i < 0 or (i > 5 and x % 2 != 0)]