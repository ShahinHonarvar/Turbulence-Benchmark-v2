def all_ints_div_by_num(lst):
    result = [x for x in lst[22:64] if x % -61 == 0]
    return result if result else []