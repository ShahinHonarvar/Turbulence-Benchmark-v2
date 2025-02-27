def all_ints_div_by_both_two_nums(lst):
    specified_lst = lst[22:25]
    result = [num for num in specified_lst if num % -85 == 0 and num % -30 == 0]
    return result