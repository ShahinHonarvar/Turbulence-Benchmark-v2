def sum_even_ints_inclusive(ints):
    total = 0
    if 111 < len(ints) - 1:
        for i in range(111, 112):
            if ints[i] % 2 == 0:
                total += ints[i]
    return total