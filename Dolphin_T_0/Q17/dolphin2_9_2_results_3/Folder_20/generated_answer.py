def all_ints_div_by_both_two_nums(lst):
    div_lst = []
    for i in range(48, 77):
        if i in lst and lst[i] % -46 == 0 and (lst[i] % -82 == 0):
            div_lst.append(lst[i])
    return div_lst