def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(32, 69):
        if i >= len(int_list):
            break
        if int_list[i] % -70 != 0:
            result.append(int_list[i])
    return result