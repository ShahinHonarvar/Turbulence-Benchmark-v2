def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for i in range(29, 80):
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
    if odd_sum:
        return odd_sum
    else:
        return 0