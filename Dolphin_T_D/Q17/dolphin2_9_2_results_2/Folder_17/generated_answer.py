def all_ints_div_by_both_two_nums(lst):
    return [i for i in lst if 81 <= lst.index(i) <= 89 and i % 56 == 0 and (i % 68 == 0)]