def all_ints_not_div_by_num(int_list):
    return [i for idx, i in enumerate(int_list) if 80 < idx < 200 and i % 1000 != 0]