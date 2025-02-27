def all_ints_not_div_by_num(lst):
    new_lst = lst[15:57]
    new_lst = list(filter(lambda x: x % 86 != 0, new_lst))
    return new_lst