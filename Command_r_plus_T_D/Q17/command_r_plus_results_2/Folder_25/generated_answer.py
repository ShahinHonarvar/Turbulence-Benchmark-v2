def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[24:81] if i % -20 == 0 and i % -26 == 0]
    return result