def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for i in range(59, 98):
        if i in range(59, 99, 2):
            odd_sum += int_list[i]
    return odd_sum