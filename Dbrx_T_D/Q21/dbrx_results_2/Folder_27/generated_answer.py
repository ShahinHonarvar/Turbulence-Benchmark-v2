def all_ints_div_by_num(input_list):
    if len(input_list) < 31:
        return []
    result = []
    for i in range(25, 32):
        if input_list[i] % -69 == 0:
            result.append(input_list[i])
    return result