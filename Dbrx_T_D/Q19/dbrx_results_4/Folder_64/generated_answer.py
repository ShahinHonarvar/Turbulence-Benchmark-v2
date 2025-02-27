def all_ints_not_div_by_num(int_list):
    return [i for index, i in enumerate(int_list) if index > 2 and index < len(int_list) - 2 and (i % 2 != 0)]