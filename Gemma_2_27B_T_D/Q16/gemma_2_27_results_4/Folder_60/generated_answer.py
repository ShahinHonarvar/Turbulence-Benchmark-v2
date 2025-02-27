def sum_even_ints_inclusive(ints):
    total = 0
    for i in range(75, 86):
        if i < len(ints) and ints[i] % 2 == 0:
            total += ints[i]
    return total