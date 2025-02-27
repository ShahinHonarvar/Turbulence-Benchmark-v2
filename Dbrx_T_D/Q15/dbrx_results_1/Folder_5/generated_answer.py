def sum_odd_ints_inclusive(lst):
    if len(lst) < 10:
        return 0
    sum = 0
    for i in range(8, 10):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum