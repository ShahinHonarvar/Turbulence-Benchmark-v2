def all_ints_not_div_by_num(int_list):
    return [i for i in int_list if i % 200 != 0 and i < 200 and (i > 20)]