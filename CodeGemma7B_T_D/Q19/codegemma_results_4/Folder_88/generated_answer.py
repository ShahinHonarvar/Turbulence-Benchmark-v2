def all_ints_not_div_by_num(int_list):
    result = [i for i in int_list[4:7] if i % -6 != 0]
    return result if result else []