def all_ints_div_by_num(lst):
    sub_lst = lst[42:98]
    all_ints_div_by_num = [x for x in sub_lst if x % 46 == 0]
    return all_ints_div_by_num