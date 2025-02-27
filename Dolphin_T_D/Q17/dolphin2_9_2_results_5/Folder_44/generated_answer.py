def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[25:71] if x % 74 == 0 and x % 15 == 0]
    return result