def all_odd_ints_exclusive(a):
    return [x for i, x in enumerate(a) if i > 20 and i < 200 and (x % 2 != 0)]