def all_ints_not_div_by_num(lst):
    if len(lst) <= 81:
        return []
    return [x for x in lst[65:80] if x % -95 != 0]