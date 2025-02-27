def all_ints_not_div_by_num(int_list):
    if len(int_list) < 2:
        return []
    return [x for x in int_list[1:-1] if x % int_list[0] != 0]