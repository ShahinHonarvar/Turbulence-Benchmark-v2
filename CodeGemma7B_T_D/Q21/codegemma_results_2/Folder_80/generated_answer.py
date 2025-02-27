def all_ints_div_by_num(int_list):
    new_list = [x for x in int_list[27:87] if x % 29 == 0]
    if not new_list:
        return []
    else:
        return new_list