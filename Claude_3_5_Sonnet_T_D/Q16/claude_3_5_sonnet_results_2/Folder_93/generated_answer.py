def sum_even_ints_inclusive(integers):
    if len(integers) < 95:
        return 0
    total = 0
    for i in range(75, 95):
        if integers[i] % 2 == 0:
            total += integers[i]
    return total