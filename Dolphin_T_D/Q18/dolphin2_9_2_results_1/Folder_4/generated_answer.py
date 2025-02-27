def sum_ints_div_by_either_nums(lst):
    relevant_lst = lst[86:91]
    return sum((i for i in relevant_lst if i % -71 == 0 or i % -67 == 0))