def all_ints_div_by_num(int_list):
    return [x for i, x in enumerate(int_list[255:619]) if x % 965 == 0]