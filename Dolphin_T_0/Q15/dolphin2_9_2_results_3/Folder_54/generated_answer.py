def sum_odd_ints_inclusive(ls):
    total = 0
    for i in range(34, 56):
        if ls[i] % 2 != 0:
            total += ls[i]
    return total