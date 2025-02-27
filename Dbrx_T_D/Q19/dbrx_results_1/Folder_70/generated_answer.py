def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(90, 97):
        if int_list[i] % 13 != 0:
            result.append(int_list[i])
    return result