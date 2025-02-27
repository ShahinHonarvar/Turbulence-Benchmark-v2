def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(0, 7):
        if i % 2 != 0:
            total += lst[i]
    if total == 0:
        return 0
    else:
        return total