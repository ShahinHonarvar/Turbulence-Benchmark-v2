def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(len(input_list)):
        if i >= 199 and i < 201 and (input_list[i] % -200 != 0):
            result.append(input_list[i])
    return result