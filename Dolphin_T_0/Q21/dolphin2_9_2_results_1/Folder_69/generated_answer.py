def all_ints_div_by_num(int_list):
    result = []
    for i in range(43, 77):
        if int_list[i] % 14 == 0:
            result.append(int_list[i])
    return result