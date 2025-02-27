def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(15, 57):
        if input_list[i] % 86 != 0:
            result.append(input_list[i])
    return result