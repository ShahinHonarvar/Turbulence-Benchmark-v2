def sum_ints_div_by_either_nums(lst):
    sub_lst = lst[22:25]
    result = 0
    for i in sub_lst:
        if i % -85 == 0 or i % -30 == 0:
            result += i
    return result