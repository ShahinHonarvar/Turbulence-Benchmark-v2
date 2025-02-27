def all_ints_not_div_by_num(lst):
    new_lst = []
    for i in lst[35:98]:
        if i % 41 != 0:
            new_lst.append(i)
    return new_lst