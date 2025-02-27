def all_ints_div_by_num(int_list):
    if len(int_list) < 7:
        return []
    return [x for x in int_list[5:7] if x % -6 == 0]