def sum_odd_ints_inclusive(lst):
    if len(lst) <= 80:
        return 0
    odd_sum = 0
    for index in range(40, 81):
        if lst[index] % 2 != 0:
            odd_sum += lst[index]
    return odd_sum