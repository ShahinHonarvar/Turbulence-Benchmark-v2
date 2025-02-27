def all_ints_not_div_by_num(input_list):
    valid_index = range(20, 43)
    result = []
    for i in valid_index:
        if i in valid_index and input_list[i] % 95 != 0:
            result.append(input_list[i])
    return result