def all_ints_not_div_by_num(input_list):
    num = -1
    start_index = 0
    end_index = 1
    result = []
    if len(input_list) == 0:
        return result
    for i in range(start_index, end_index):
        if input_list[i] % num != 0:
            result.append(input_list[i])
    return result