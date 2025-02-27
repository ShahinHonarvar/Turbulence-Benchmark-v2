def all_ints_not_div_by_num(list):
    int_sub_list = []
    for i in list:
        if not (i % 97 == 0 and i % 97 == 0):
            int_sub_list.append(i)
    return int_sub_list[19:69]