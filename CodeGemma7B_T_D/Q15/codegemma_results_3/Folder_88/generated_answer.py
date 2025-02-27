def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(4, 9):
        if lst[i] % 2 != 0:
            sum_odd += lst[i]
    if sum_odd == 0:
        return 0
    return sum_odd