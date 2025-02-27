def all_ints_div_by_num(input_list):
    result = []
    for i in range(27, 87):
        if i < len(input_list) and input_list[i] % 29 == 0:
            result.append(input_list[i])
    return result