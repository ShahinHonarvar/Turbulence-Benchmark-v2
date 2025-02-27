def sum_odd_ints_inclusive(ints):
    sum = 0
    if 23 < len(ints) and ints[23] % 2 != 0:
        sum += ints[23]
    return sum