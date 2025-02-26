def sum_odd_ints_inclusive(integers):
    if not integers:
        return 0
    return integers[0] if integers[0] % 2 != 0 else 0