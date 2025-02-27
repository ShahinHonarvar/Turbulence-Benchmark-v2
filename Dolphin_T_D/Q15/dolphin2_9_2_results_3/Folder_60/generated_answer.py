def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(75, 86):
        if lst[i] % 2 != 0:
            total += lst[i]
    if total == 0:
        return 0
    else:
        return total