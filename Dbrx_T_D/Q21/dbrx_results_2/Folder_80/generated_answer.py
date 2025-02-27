def all_ints_div_by_num(int_list):
    result = []
    for i in range(27, 87):
        if len(int_list) > i and int_list[i] % 29 == 0:
            result.append(int_list[i])
    return result