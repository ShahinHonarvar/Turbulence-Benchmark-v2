def all_ints_not_div_by_num(int_list):
    num = 1
    result = []
    for i in range(len(int_list)):
        if i != 0 and i != 1 and (int_list[i] % num != 0):
            result.append(int_list[i])
    return result