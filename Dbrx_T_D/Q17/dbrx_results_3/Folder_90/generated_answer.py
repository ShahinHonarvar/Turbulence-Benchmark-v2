def all_ints_div_by_both_two_nums(int_list):
    start_index = 138
    end_index = 424
    target_divisor_1 = -863
    target_divisor_2 = -329
    result = []
    for i in range(start_index, end_index + 1):
        if int_list[i] % target_divisor_1 == 0 and int_list[i] % target_divisor_2 == 0:
            result.append(int_list[i])
    return result