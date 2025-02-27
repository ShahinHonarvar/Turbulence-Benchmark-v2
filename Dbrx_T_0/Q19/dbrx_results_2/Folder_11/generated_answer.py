def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(36, 85):
        if i >= len(input_list):
            break
        if input_list[i] % -27 != 0:
            result.append(input_list[i])
    return result