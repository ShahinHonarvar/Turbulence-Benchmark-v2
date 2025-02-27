def all_ints_div_by_both_two_nums(lst):
    ret_lst = []
    for i in range(828, 933):
        if i in lst and i % -649 == 0 and (i % -461 == 0):
            ret_lst.append(i)
    return ret_lst