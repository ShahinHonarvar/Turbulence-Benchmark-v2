def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(len(input_list)):
        if i >= 19 and i < 49 and (input_list[i] % -36 != 0):
            result.append(input_list[i])
    return result