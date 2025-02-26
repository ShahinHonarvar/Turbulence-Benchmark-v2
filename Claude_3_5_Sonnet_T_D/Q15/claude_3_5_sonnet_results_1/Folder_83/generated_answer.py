def sum_odd_ints_inclusive(integer_list):
    start_index = 90
    end_index = 200
    odd_sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list):
            if integer_list[i] % 2 != 0:
                odd_sum += integer_list[i]
    return odd_sum