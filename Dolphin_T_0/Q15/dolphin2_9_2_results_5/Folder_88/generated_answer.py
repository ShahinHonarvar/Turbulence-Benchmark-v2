def sum_odd_ints_inclusive(ints):
    total = 0
    for i in range(4, 9):
        if ints[i] % 2 == 1:
            total += ints[i]
    return total if total else 0