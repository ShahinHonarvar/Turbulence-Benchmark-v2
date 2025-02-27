def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[:3] if x % -2 == 0 and x % 3 == 0]
    return result