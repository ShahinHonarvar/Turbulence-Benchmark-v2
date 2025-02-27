def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[22:89], 22) if x % 2 == 1]