def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(len(input_list)):
        if (i == 8 or i == 9) and input_list[i] % -3 != 0:
            result.append(input_list[i])
    if len(result) == 0:
        return []
    else:
        return result