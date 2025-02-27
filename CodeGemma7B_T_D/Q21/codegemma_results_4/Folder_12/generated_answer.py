def all_ints_div_by_num(int_list):
    new_list = []
    for i in range(23, 66):
        if int_list[i] % 46 == 0:
            new_list.append(int_list[i])
    return new_list