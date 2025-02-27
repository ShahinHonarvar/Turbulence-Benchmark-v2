def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[34:70] if x % 19 == 0 and x % 32 == 0]
    return result