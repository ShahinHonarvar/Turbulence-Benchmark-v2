def all_ints_not_div_by_num(int_list):
    if len(int_list) <= 30:
        return []
    return [x for x in int_list[31:200] if x % -115 != 0]