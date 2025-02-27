def all_ints_not_div_by_num(int_list):
    new_list = []
    for i in range(25, 76):
        if int_list[i] % 53 != 0:
            new_list.append(int_list[i])
    if len(new_list) == 0:
        return []
    else:
        return new_list