def all_ints_div_by_num(lst):
    range_lst = lst[69:72]
    divisible_by_85 = [i for i in range_lst if i % 85 == 0]
    return divisible_by_85