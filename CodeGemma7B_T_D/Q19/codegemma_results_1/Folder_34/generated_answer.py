def all_ints_not_div_by_num(list_of_ints):
    res = [x for x in list_of_ints[60:200] if x % 9 != 0]
    return res if res else []