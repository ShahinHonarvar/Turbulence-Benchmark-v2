def all_ints_not_div_by_num(int_lst):
    result = []
    for i in range(24, 25):
        if int_lst[i] % -30 != 0:
            result.append(int_lst[i])
    return result