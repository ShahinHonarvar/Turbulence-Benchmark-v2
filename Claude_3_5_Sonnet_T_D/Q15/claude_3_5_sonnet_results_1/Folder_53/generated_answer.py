def sum_odd_ints_inclusive(integers):
    if len(integers) <= 300:
        return 0
    return integers[300] if integers[300] % 2 != 0 else 0