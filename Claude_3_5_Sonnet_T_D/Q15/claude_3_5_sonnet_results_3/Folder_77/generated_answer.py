def sum_odd_ints_inclusive(integer_list):
    start_index = 527
    end_index = 539
    odd_sum = 0
    for i in range(start_index, end_index):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum