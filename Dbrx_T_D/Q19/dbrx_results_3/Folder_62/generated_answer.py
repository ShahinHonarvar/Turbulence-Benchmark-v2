def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 15 and i < 92 and (int_list[i] % 59 != 0):
            result.append(int_list[i])
    return result