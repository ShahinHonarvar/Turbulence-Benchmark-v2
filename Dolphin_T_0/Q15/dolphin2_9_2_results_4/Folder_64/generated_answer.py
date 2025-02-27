def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(5):
        if lst[i] % 2 == 1:
            total += lst[i]
    if total == 0:
        return 0
    else:
        return total