def all_ints_not_div_by_num(lst):
    spl = lst[70:200]
    ret = [x for x in spl if x % -300 != 0]
    return ret if ret else []