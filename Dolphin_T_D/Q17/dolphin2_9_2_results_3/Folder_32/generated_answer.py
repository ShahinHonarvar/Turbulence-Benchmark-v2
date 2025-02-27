def all_ints_div_by_both_two_nums(lst):
    sub_lst = lst[25:96]
    res_lst = [i for i in sub_lst if i % 51 == 0 and i % 77 == 0]
    return res_lst