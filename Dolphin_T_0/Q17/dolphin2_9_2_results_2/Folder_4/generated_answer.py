def all_ints_div_by_both_two_nums(lst):
    range_lst = lst[86:91]
    result = [num for num in range_lst if num % -71 == 0 and num % -67 == 0]
    return result