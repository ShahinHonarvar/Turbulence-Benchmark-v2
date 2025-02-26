def sum_odd_ints_inclusive(lst):
    if len(lst) <= 63:
        return 0
    odd_sum = 0
    for i in range(22, 64):
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
    return odd_sum