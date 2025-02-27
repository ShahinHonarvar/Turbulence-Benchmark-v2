def all_ints_not_div_by_num(lst):
    result = [x for x in lst[8:9] if x % -3 != 0]
    return result if result else []