def all_ints_not_div_by_num(lst):
    result = [x for x in lst[21:200] if x % -200 != 0]
    return result