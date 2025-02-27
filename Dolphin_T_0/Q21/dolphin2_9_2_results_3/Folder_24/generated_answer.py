def all_ints_div_by_num(lst):
    res = [item for item in lst[12:78] if item % -19 == 0]
    return res if res else []