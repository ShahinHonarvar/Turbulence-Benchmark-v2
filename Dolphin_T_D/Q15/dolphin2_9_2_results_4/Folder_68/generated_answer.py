def sum_odd_ints_inclusive(integers):
    total = 0
    for i in range(0, 9):
        if integers[i] % 2 != 0:
            total += integers[i]
    return total