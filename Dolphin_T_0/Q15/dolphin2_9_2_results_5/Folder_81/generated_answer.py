def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(10, 101):
        if i % 2 != 0:
            total += lst[i]
    return total