def all_ints_div_by_both_two_nums(lst):
    div_by_both = [i for i in lst[250:630] if i % 850 == 0 and i % 587 == 0]
    return div_by_both