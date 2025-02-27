def all_ints_div_by_num(int_list):
    if len(int_list) < 41:
        return []
    else:
        return [i for i in int_list[35:41] if i % 28 == 0]