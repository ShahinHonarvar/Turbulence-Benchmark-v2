def all_ints_not_div_by_num(lst):
    new_lst = []
    for i in range(64, 74):
        if lst[i] % -99 != 0:
            new_lst.append(lst[i])
    return new_lst