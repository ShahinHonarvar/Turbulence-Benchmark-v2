def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(25, 88):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total