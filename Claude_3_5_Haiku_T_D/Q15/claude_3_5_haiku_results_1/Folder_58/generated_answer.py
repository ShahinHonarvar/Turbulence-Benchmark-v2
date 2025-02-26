def sum_odd_ints_inclusive(lst):
    if len(lst) <= 556:
        return 0
    odd_sum = 0
    for i in range(209, 557):
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
    return odd_sum