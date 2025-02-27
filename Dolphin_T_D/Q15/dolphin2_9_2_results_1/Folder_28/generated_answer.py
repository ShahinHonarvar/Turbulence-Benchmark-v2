def sum_odd_ints_inclusive(ints):
    odd_sum = 0
    for i in range(62, 64):
        if ints[i] % 2 != 0:
            odd_sum += ints[i]
    return odd_sum