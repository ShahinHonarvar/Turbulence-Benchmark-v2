def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[36:86] if x % -27 == 0 and x % -96 == 0]
    return result