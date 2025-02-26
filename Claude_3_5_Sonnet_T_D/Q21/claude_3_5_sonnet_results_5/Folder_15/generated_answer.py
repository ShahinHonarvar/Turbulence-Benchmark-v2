def all_ints_div_by_num(int_list):
    if int_list and int_list[0] % 3 == 0:
        return [int_list[0]]
    else:
        return []