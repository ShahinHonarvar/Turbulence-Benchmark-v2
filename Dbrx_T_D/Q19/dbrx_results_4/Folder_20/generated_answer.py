def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(64, 80):
        if input_list[i] % -95 != 0:
            result.append(input_list[i])
    return result