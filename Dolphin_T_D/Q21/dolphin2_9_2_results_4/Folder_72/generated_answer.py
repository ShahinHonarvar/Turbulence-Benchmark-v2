def all_ints_div_by_num(lst):
    range_lst = lst[11:83]
    divisible_nums = [i for i in range_lst if i % -47 == 0]
    return divisible_nums