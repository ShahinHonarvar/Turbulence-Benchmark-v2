def all_ints_div_by_both_two_nums(lst):
    div_by_both = [i for i in lst[20:36] if i % -36 == 0 and i % -89 == 0]
    return div_by_both