def all_ints_div_by_num(int_list):
    if len(int_list) <= 8:
        return []
    if int_list[8] % -7 == 0:
        return [int_list[8]]
    return []