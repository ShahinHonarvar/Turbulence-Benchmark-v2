def all_ints_not_div_by_num(lst):
    if len(lst) <= 905:
        return []
    return [x for x in lst[768:905] if x % -430 != 0]