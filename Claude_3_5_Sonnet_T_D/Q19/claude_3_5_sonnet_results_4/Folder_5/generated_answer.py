def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(2, len(int_list) - 1):
        if int_list[i] % 8 != 0:
            result.append(int_list[i])
    return result