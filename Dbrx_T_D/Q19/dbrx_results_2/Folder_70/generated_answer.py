def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(len(input_list)):
        if i >= 90 and i < 97 and (input_list[i] % 13 != 0):
            result.append(input_list[i])
    return result