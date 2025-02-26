def all_ints_div_by_num(int_list):
    if len(int_list) <= 10:
        return []
    return [int_list[10]] if int_list[10] % 1 == 0 else []