def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 25 and i < 80 and (x % 2 != 0)]