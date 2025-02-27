def all_ints_div_by_both_two_nums(lst):
    return [i for i in lst[80:201] if not i % 10 and (not i % 1000)]