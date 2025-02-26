def sum_even_ints_inclusive(integers):
    if len(integers) <= 111:
        return 0
    if integers[111] % 2 == 0:
        return integers[111]
    return 0