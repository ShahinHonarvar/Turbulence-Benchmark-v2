def sum_odd_ints_inclusive(ints):
    total = 0
    for i in range(70, 201):
        if ints[i] % 2 != 0:
            total += ints[i]
    return total