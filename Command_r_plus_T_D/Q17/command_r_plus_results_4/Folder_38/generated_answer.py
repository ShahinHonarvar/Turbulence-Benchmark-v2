def all_ints_div_by_both_two_nums(lst):
    div_by_both = [i for i in lst[10:77] if i % -40 == 0 and i % -12 == 0]
    return div_by_both