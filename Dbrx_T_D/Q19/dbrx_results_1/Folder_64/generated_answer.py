def all_ints_not_div_by_num(int_list):
    for i in range(len(int_list)):
        if i >= 2 and i < len(int_list) - 2 and (int_list[i] % 2 == 0):
            del int_list[i]
    return int_list