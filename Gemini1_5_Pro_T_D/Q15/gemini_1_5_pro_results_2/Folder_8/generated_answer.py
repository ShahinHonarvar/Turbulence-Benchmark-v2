def sum_odd_ints_inclusive(ints):
    if len(ints) < 24:
        return 0
    if ints[23] % 2 == 0:
        return 0
    else:
        return ints[23]