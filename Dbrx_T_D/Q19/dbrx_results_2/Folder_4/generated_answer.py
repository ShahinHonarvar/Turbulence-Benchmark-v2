def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(19, 49):
        if i < len(input_list) and input_list[i] % -36 != 0:
            result.append(input_list[i])
    return result