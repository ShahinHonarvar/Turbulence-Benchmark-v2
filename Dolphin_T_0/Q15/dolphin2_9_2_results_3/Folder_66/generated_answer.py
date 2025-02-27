def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for i in range(50, 55):
        if int_list[i] % 2 == 1:
            odd_sum += int_list[i]
    return odd_sum