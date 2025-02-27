def all_ints_div_by_num(input_list):
    result = []
    if len(input_list) < 93:
        return result
    for i in range(86, 93):
        if input_list[i] % 86 == 0:
            result.append(input_list[i])
    return result