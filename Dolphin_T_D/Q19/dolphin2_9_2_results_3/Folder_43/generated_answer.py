def all_ints_not_div_by_num(lst):
    result = [i for i in lst[16:87] if i % -15 != 0]
    return result if result else []