def all_odd_ints_exclusive(l):
    return [x for i, x in enumerate(l) if i > 13 and i < 76 and (x % 2 != 0)]