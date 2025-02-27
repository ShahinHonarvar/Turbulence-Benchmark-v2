def all_ints_div_by_both_two_nums(lst):
    new_lst = []
    for i in lst[13:77]:
        if i % -66 == 0 and i % -32 == 0:
            new_lst.append(i)
    if new_lst == []:
        return []
    else:
        return new_lst