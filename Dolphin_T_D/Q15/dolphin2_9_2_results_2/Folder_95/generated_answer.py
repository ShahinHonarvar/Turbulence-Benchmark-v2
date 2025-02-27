def sum_odd_ints_inclusive(lis):
    total = 0
    for i in range(82, 87):
        if lis[i] % 2 != 0:
            total += lis[i]
    return total or 0