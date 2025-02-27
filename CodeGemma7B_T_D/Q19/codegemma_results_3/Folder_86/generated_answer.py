def all_ints_not_div_by_num(int_list):
    new_list = []
    for i in range(15, 63):
        if int_list[i] % 34 != 0:
            new_list.append(int_list[i])
    return new_list