def all_ints_div_by_num(lst):
    result = [x for x in lst[319:613] if x % -215 == 0]
    return result if result else []