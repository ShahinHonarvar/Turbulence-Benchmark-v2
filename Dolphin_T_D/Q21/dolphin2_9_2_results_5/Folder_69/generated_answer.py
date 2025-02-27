def all_ints_div_by_num(lst):
    result = [x for x in lst[43:77] if x % 14 == 0]
    return result if result else []