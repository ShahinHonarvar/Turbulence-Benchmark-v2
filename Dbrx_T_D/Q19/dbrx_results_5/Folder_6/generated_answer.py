def all_ints_not_div_by_num(int_list):
    return [i for i in int_list[43:70] if i % 69 != 0] if len(int_list) >= 70 else []