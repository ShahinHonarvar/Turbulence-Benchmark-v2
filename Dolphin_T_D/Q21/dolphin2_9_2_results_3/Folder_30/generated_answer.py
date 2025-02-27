def all_ints_div_by_num(lst):
    div_lst = [i for i in lst[59:80] if i % -82 == 0]
    return div_lst if len(div_lst) > 0 else []