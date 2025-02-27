def all_odd_ints_exclusive(ints):
    return [n for i, n in enumerate(ints) if i > 42 and i < 99 and (n % 2 != 0)]