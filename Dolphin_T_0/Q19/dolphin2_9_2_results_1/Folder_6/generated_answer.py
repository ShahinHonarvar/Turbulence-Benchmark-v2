def all_ints_not_div_by_num(lst):
    range_lst = lst[43:70]
    result = [i for i in range_lst if i % 69 != 0]
    return result