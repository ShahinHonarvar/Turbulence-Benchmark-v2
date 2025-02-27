def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(len(input_list)):
        if i >= 46 and i < 91 and (input_list[i] % 67 != 0):
            result.append(input_list[i])
    return result