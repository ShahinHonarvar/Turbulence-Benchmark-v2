def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(82, 87):
        if lst[i] % 2 == 1:
            total += lst[i]
    return total