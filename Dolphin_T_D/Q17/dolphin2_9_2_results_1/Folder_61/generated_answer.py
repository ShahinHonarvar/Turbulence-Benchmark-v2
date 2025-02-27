def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[:7] if i % -5 == 0 and i % -6 == 0]
    return result if result else []