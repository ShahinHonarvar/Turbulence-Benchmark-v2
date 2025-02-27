def all_ints_not_div_by_num(lst):
    result = [x for x in lst[30:200] if x % -115 != 0]
    return result