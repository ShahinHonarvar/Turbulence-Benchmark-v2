def all_ints_not_div_by_num(int_list):
    res = [i for i in int_list[7:9] if i % -9 != 0]
    return res if res else []