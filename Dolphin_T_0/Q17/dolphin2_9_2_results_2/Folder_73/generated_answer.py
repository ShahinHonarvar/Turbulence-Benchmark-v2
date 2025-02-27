def all_ints_div_by_both_two_nums(lst):
    specified_range = lst[81:87]
    result = [i for i in specified_range if i % -33 == 0 and i % -62 == 0]
    return result