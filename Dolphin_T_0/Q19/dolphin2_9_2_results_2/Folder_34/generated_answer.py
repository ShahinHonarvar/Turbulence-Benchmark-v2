def all_ints_not_div_by_num(lst):
    return [val.index(i) for i in lst[60:200] if i % 9 != 0]