def all_ints_div_by_both_two_nums(lst):
    div_by_both = [i for i in lst[10:80] if i % -74 == 0 and i % -58 == 0]
    return div_by_both