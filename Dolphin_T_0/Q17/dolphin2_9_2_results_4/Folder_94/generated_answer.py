def all_ints_div_by_both_two_nums(lst):
    specified_range = lst[93:95]
    result = [i for i in specified_range if i % -53 == 0 and i % -91 == 0]
    return result