def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(50, 201):
        if i % 2 != 0:
            total += lst[i]
    return total or 0