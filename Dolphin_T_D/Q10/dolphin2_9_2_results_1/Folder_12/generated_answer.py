def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(24, 46) and x % 2 == 1]