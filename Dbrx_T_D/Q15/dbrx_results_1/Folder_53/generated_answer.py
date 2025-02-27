def sum_odd_ints_inclusive(int_list):
    start_index = min(299, len(int_list) - 1)
    end_index = min(300, len(int_list) - 1)
    odd_ints_sum = 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 != 0:
            odd_ints_sum += int_list[i]
    return odd_ints_sum