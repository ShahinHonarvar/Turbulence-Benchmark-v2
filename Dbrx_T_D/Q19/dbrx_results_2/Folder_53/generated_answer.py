def all_ints_not_div_by_num(input_list):
    start_index = 199
    end_index = 201
    result = []
    for i in range(start_index, end_index):
        if len(input_list) > i and input_list[i] % -200 != 0:
            result.append(input_list[i])
    return result