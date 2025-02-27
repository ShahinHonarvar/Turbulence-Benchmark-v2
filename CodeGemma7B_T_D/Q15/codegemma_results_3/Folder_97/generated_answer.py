def sum_odd_ints_inclusive(list1):
    odd_sum = 0
    for i in range(40, 81):
        if list1[i] % 2 != 0:
            odd_sum += list1[i]
    if odd_sum == 0:
        return 0
    else:
        return odd_sum