def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[7:10] if x % -9 == 0 and x % -7 == 0]
    return result