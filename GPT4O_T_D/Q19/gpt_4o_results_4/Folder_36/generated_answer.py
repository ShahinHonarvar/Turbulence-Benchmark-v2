def all_ints_not_div_by_num(lst):
    if len(lst) < 827:
        return []
    return [x for x in lst[473:827] if x % 602 != 0]