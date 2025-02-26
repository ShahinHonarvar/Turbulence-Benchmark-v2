def sum_even_ints_inclusive(integers):
    if len(integers) < 35:
        return 0
    total = 0
    for i in range(31, 35):
        if integers[i] % 2 == 0:
            total += integers[i]
    return total