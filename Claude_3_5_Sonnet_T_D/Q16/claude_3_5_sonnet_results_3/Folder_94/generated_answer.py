def sum_even_ints_inclusive(integer_list):
    start_index = 28
    end_index = 40
    total_sum = 0
    if len(integer_list) <= start_index:
        return 0
    for i in range(start_index, min(end_index + 1, len(integer_list))):
        if integer_list[i] % 2 == 0:
            total_sum += integer_list[i]
    return total_sum