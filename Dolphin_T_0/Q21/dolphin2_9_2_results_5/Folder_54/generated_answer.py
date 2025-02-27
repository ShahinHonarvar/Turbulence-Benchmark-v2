def all_ints_div_by_num(lst):
    a = [x for x in lst[31:73] if x % -63 == 0]
    return a if len(a) != 0 else []