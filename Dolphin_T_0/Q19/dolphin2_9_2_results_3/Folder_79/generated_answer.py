def all_ints_not_div_by_num(lst):
    new_lst = []
    for i in lst[8:9]:
        if i % -3 != 0:
            new_lst.append(i)
    return new_lst