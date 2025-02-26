def sum_odd_ints_inclusive(integers):
    if len(integers) <= 82:
        return 0
    odd_sum = 0
    for i in range(56, 83):
        if integers[i] % 2 != 0:
            odd_sum += integers[i]
    return odd_sum