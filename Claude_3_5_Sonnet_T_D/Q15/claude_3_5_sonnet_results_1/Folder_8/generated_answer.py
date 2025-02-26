def sum_odd_ints_inclusive(integers):
    if len(integers) <= 23:
        return 0
    if integers[23] % 2 != 0:
        return integers[23]
    return 0