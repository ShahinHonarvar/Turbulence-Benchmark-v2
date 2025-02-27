def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(209, 557):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total