def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[22:25] if i % -85 == 0 and i % -30 == 0]
    return result if result else []