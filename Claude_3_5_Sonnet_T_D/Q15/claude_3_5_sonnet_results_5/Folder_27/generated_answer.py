def sum_odd_ints_inclusive(integers):
    odd_sum = 0
    for i in range(66, 94):
        if i < len(integers) and integers[i] % 2 != 0:
            odd_sum += integers[i]
    return odd_sum