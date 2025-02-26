def all_ints_div_by_num(int_list):
    if not int_list:
        return []
    return [int_list[0]] if int_list[0] % 4 == 0 else []