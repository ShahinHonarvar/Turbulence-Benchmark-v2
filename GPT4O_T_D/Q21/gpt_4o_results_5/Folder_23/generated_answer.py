def all_ints_div_by_num(lst):
    if len(lst) < 98:
        return []
    return [x for x in lst[59:98] if x % -36 == 0]