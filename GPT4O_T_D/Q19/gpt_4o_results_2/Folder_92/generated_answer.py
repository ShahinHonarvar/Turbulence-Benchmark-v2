def all_ints_not_div_by_num(lst):
    if len(lst) <= 2:
        return []
    return [x for x in lst[1:-1] if x % -1 != 0]