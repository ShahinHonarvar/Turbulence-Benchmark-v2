def all_even_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 13 and i <= 68 and (x % 2 == 0)]