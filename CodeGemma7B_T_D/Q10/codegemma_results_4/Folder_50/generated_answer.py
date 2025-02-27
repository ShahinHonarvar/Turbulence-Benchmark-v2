def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 70 and i <= 98 and (x % 2 != 0)]