def all_ints_div_by_num(int_list):
    if len(int_list) < 53:
        return []
    result = []
    for i in range(52, 54):
        if int_list[i] % 93 == 0:
            result.append(int_list[i])
    return result