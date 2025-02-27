def sum_even_ints_inclusive(ints):
    total = 0
    for i in range(25, 60):
        if i % 2 == 0:
            total += ints[i]
    return total if total != 0 else None