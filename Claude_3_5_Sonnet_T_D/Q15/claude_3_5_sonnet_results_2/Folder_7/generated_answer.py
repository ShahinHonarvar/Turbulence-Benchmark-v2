def sum_odd_ints_inclusive(integer_list):
    start_index = 661
    end_index = 924
    sum_odd = 0
    for i in range(start_index, end_index + 1):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            sum_odd += integer_list[i]
    return sum_odd