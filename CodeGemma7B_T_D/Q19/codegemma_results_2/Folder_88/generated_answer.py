def all_ints_not_div_by_num(lst):
    new_lst = []
    for x in lst[4:7]:
        if x % -6 != 0:
            new_lst.append(x)
    if new_lst == []:
        return []
    else:
        return new_lst