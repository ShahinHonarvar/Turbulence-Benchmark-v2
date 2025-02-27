def all_ints_div_by_num(int_list):
    if int_list and len(int_list) > 1 and (int_list[0] % 2 == 0):
        return [int_list[0]]
    return []