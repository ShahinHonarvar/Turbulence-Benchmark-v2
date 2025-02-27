def all_ints_div_by_both_two_nums(lst):
    range_lst = lst[25:71]
    result = [x for x in range_lst if x % 74 == 0 and x % 15 == 0]
    return result