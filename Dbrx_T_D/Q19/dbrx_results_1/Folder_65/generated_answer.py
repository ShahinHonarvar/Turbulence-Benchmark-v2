def all_ints_not_div_by_num(input_list):
    start_index = 15
    end_index = 51
    result = []
    for i in range(start_index, end_index):
        if input_list[i] % -34 != 0:
            result.append(input_list[i])
    return result