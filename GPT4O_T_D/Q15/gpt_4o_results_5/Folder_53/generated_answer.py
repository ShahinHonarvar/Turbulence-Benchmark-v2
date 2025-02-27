def sum_odd_ints_inclusive(integers):
    if len(integers) <= 300:
        return 0
    return sum((i for i in integers[300:301] if i % 2 != 0))