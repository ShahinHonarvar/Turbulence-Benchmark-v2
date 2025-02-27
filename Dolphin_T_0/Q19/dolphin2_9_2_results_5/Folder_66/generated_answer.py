def all_ints_not_div_by_num(lst):
    result = [x for x in lst[84:86] if x % 99 != 0]
    return result if result else []