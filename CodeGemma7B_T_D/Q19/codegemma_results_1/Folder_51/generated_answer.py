def all_ints_not_div_by_num(int_list):
    res = []
    for i in range(1, 6):
        if int_list[i] % 2 != 0:
            res.append(int_list[i])
    return res