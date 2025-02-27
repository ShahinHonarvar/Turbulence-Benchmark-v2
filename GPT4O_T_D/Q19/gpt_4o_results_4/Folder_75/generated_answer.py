def all_ints_not_div_by_num(int_list):
    if len(int_list) <= 21:
        return []
    return [x for x in int_list[21:51] if x % -48 != 0]