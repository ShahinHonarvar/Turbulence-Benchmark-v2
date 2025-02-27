def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i not in range(68, 100) and x % 2 == 1]