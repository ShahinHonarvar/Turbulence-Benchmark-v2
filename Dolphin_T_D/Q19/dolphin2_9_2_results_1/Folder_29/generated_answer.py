def all_ints_not_div_by_num(lst):
    range_lst = lst[24:25]
    res = [i for i in range_lst if i % -30 != 0]
    return res