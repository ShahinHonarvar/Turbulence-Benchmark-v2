def all_ints_div_by_num(int_list):
    if len(int_list) == 0:
        return []
    return [int_list[0]] if int_list[0] % 2 == 0 else []