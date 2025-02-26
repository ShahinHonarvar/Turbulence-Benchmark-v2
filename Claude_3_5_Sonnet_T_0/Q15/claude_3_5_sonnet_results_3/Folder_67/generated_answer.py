def sum_odd_ints_inclusive(integer_list):
    start_index = 22
    end_index = 51
    odd_sum = 0
    if len(integer_list) > start_index:
        for num in integer_list[start_index:end_index]:
            if num % 2 != 0:
                odd_sum += num
    return odd_sum