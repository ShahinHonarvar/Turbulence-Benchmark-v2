def all_ints_not_div_by_num(lst):
    if len(lst) <= 57:
        return []
    return [x for x in lst[57:88] if x % -59 != 0]