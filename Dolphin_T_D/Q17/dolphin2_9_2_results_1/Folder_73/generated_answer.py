def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[81:87] if i % -33 == 0 and i % -62 == 0]
    return result if result else []