def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[:9] if i % -3 == 0 and i % 8 == 0]
    return result