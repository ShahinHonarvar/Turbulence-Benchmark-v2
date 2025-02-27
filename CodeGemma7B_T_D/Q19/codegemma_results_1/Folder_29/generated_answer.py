def all_ints_not_div_by_num(int_lst):
    lst = []
    for i in range(24, 25):
        if int_lst[i] % -30 != 0:
            lst.append(int_lst[i])
    return lst