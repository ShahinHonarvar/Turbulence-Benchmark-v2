def all_ints_div_by_both_two_nums(lst):
    div_by_both = [i for i in lst[38:82] if i % -61 == 0 and i % -71 == 0]
    return div_by_both