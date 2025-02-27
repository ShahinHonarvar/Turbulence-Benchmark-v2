def all_even_ints_exclusive(ints):
    return [n for i, n in enumerate(ints) if i > 12 and i < 76 and (n % 2 == 0)]