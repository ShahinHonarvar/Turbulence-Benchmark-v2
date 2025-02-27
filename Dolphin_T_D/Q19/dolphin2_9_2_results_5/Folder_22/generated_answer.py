def all_ints_not_div_by_num(lst):
    result = [x for x in lst[40:200] if x % 71 != 0]
    return result if result else []