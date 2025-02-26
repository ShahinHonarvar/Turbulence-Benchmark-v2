def sum_odd_ints_inclusive(integer_list):
    start_index = 31
    end_index = 73
    odd_sum = 0
    for i in range(start_index, end_index):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum