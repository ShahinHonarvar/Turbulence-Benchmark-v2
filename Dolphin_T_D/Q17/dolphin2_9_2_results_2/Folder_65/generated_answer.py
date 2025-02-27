def all_ints_div_by_both_two_nums(lst):
    sublist = lst[50:93]
    result = [i for i in sublist if i % -94 == 0 and i % -95 == 0]
    return result