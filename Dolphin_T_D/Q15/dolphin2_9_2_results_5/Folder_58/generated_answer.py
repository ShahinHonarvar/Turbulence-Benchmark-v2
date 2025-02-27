def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(209, 557):
        if i % 2 != 0 and i < len(lst):
            total += lst[i]
    return total