def sum_odd_ints_inclusive(int_list):
    odd_ints_sum = 0
    for idx in range(29, 80):
        if idx % 2 != 0:
            odd_ints_sum += int_list[idx]
    return odd_ints_sum