def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(59, 98) and x % 2 == 1]