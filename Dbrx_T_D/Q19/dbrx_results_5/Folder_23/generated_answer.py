def all_ints_not_div_by_num(input_list):
    num = -68
    start_index = 44
    end_index = 91
    result = []
    for i in range(start_index, end_index):
        if input_list[i] % num != 0:
            result.append(input_list[i])
    return result