def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(26, 80) and x % 2 != 0]