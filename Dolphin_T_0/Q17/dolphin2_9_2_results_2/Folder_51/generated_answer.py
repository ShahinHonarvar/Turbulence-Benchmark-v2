def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[5:10] if x % -1 == 0 and x % -10 == 0]
    return result