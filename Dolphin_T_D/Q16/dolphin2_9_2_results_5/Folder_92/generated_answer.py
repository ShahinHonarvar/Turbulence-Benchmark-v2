def sum_even_ints_inclusive(ints):
    if not ints:
        return 0
    if len(ints) == 1:
        return ints[0] if ints[0] % 2 == 0 else 0
    return ints[0] + ints[1] if ints[0] % 2 == 0 and ints[1] % 2 == 0 else ints[0] + ints[1] - ints[1]