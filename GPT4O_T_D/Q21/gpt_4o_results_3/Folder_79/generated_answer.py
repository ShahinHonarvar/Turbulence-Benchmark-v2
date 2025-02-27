def all_ints_div_by_num(int_list):
    if len(int_list) < 9:
        return []
    return [x for x in int_list[8:9] if x % -7 == 0]