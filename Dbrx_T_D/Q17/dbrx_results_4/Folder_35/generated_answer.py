def all_ints_div_by_both_two_nums(input_list):
    result = []
    start_index = 77
    end_index = 87
    for i in range(start_index, end_index + 1):
        if i < len(input_list) and input_list[i] % 23 == 0 and (input_list[i] % 57 == 0):
            result.append(input_list[i])
    return result