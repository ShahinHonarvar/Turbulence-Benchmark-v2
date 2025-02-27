def all_ints_div_by_num(lst):
    range_lst = lst[87:90]
    divisible_by_55 = [i for i in range_lst if i % 55 == 0]
    return divisible_by_55