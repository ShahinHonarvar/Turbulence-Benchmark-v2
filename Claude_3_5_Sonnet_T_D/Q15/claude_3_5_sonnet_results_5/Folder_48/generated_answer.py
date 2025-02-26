def sum_odd_ints_inclusive(integer_list):
    start_index = max(533, 0)
    end_index = min(605, len(integer_list) - 1)
    odd_sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum