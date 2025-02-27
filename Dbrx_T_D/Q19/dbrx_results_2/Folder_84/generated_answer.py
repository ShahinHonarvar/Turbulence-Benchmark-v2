def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(50, 81):
        if i < len(input_list) and input_list[i] % 64 != 0:
            result.append(input_list[i])
    return result