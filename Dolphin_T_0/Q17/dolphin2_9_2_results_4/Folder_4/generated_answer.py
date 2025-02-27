def all_ints_div_by_both_two_nums(lst):
    sublist = lst[86:91]
    result = [i for i in sublist if i % -71 == 0 and i % -67 == 0]
    return result if result else []