def sum_odd_ints_inclusive(int_list):
    odd_ints_sum = 0
    for i in range(74, 96):
        if i >= len(int_list):
            break
        if int_list[i] % 2 != 0:
            odd_ints_sum += int_list[i]
    return odd_ints_sum