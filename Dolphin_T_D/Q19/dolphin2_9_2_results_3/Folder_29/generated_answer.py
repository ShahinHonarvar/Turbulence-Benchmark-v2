def all_ints_not_div_by_num(int_list):
    ints_not_div_by_num = []
    for i in range(24, 26):
        if i in int_list and i % -30 != 0:
            ints_not_div_by_num.append(i)
    return ints_not_div_by_num