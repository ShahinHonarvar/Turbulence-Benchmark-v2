def all_ints_div_by_both_two_nums(int_list):
    start_index = 25
    end_index = 95
    result_list = []
    for i in range(start_index, end_index + 1):
        if i < len(int_list) and int_list[i] % 51 == 0 and (int_list[i] % 77 == 0):
            result_list.append(int_list[i])
    return result_list