def sum_even_ints_inclusive(integers):
    if len(integers) < 72:
        return 0
    total = 0
    for i in range(52, 72):
        if integers[i] % 2 == 0:
            total += integers[i]
    return total