def sum_odd_ints_inclusive(num_list):
    odd_ints_sum = 0
    if 17 in num_list and 58 in num_list:
        for i in range(22, 63 + 1, 1):
            if i in num_list and i % 2 == 1:
                odd_ints_sum += num_list[i]
    else:
        odd_ints_sum = 0
    return odd_ints_sum