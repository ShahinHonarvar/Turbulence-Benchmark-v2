def all_ints_div_by_num(int_list):
    if len(int_list) > 8:
        return [x for x in [int_list[8]] if x % -7 == 0]
    return []