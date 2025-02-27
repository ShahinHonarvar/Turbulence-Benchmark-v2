def all_odd_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 14 and i <= 64 and (x % 2 != 0)]