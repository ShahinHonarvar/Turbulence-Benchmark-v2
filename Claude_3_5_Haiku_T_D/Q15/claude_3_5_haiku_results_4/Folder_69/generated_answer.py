def sum_odd_ints_inclusive(lst):
    if len(lst) <= 35:
        return 0
    odd_sum = 0
    for i in range(32, 36):
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
    return odd_sum