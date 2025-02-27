def sum_odd_ints_inclusive(integers):
    if len(integers) < 49:
        return 0
    return sum((i for i in integers[30:49] if i % 2 != 0))