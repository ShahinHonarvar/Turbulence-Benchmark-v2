def all_ints_not_div_by_num(lst):
    result = [x for x in lst[90:200] if x % -31 != 0]
    return result