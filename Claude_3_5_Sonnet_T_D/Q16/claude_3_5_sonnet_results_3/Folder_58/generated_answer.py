def sum_even_ints_inclusive(integer_list):
    start_index = 209
    end_index = 557
    total_sum = 0
    for i in range(start_index, end_index):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            total_sum += integer_list[i]
    return total_sum