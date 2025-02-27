def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(38, 81):
        if i % 49 != 0:
            result.append(int_list[i])
    return result