def all_ints_div_by_num(int_list):
    result = []
    for i in range(572, 807):
        if i < len(int_list) and int_list[i] % -158 == 0:
            result.append(int_list[i])
    return result