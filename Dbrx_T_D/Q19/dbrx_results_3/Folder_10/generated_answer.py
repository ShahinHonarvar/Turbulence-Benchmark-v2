def all_ints_not_div_by_num(input_list):
    num = -61
    start_index = 86
    end_index = 89
    result = []
    for i in range(len(input_list)):
        if input_list[i] % num != 0 and i >= start_index and (i < end_index):
            result.append(input_list[i])
    return result