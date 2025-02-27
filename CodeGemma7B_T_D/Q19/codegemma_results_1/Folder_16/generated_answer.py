def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(24, 32):
        if int_list[i] % 35 != 0:
            result.append(int_list[i])
    return result