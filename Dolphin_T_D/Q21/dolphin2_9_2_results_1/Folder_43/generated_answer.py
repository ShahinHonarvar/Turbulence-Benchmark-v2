def all_ints_div_by_num(lst):
    subset = lst[10:37]
    return [i for i in subset if i % -64 == 0]