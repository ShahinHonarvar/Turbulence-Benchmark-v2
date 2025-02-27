def all_ints_not_div_by_num(lst):
    result = [x for x in lst[10:55] if x % 36 != 0]
    return result