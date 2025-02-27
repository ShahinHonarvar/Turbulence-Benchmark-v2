def all_ints_not_div_by_num(lst):
    result = [x for x in lst[668:739] if x % -172 != 0]
    return result if result else []