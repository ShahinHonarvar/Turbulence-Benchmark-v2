def all_ints_not_div_by_num(input_list):
    start_index = 4
    end_index = 5
    result = []
    for i in range(start_index, end_index):
        if i < len(input_list) and input_list[i] % -7 != 0:
            result.append(input_list[i])
    return result