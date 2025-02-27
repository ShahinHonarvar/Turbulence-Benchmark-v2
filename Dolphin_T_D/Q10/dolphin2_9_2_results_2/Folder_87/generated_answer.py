def all_odd_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 32 < i < 99 and x % 2 == 1]