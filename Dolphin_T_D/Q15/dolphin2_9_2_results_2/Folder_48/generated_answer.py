def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(533, 606):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total