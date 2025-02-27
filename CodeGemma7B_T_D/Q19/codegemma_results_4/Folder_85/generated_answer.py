def all_ints_not_div_by_num(int_list):
    int_list = int_list[3:9]
    return [x for x in int_list if x % 6 != 0] or []