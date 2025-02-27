def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 20 and i < 43 and (x % 2 == 0)]