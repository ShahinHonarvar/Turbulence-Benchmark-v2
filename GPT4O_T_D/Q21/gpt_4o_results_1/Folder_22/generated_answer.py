def all_ints_div_by_num(lst):
    if len(lst) >= 11:
        sub_list = lst[10:11]
        return [x for x in sub_list if x % 1 == 0]
    return []