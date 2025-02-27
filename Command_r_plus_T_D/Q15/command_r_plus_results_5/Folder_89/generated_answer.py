def sum_odd_ints_inclusive(int_list):
    if len(int_list) <= 82:
        return 0
    odd_sum = 0
    for i in range(56, 83):
        if int_list[i] % 2 != 0:
            odd_sum += int_list[i]
    return odd_sum