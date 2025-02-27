def all_ints_div_by_both_two_nums(lst):
    sub_lst = lst[14:94]
    result = [i for i in sub_lst if i % 71 == 0 and i % 81 == 0]
    return result