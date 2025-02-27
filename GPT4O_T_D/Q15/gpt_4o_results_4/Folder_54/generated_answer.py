def sum_odd_ints_inclusive(integers):
    if len(integers) < 56:
        return 0
    return sum((i for i in integers[34:56] if i % 2 != 0))