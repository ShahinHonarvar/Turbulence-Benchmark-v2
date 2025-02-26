def sum_odd_ints_inclusive(integer_list):
    start_index = 34
    end_index = 56
    odd_sum = 0
    if len(integer_list) <= start_index:
        return 0
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum