def sum_odd_ints_inclusive(list):
    total = 0
    for i in range(28, 33):
        if list[i] % 2 != 0:
            total += list[i]
    return total or 0