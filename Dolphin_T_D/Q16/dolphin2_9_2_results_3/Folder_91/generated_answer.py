def sum_even_ints_inclusive(ints):
    total = 0
    if len(ints) > 5:
        for i in range(6):
            if ints[i] % 2 == 0:
                total += ints[i]
    return total