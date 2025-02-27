def all_ints_div_by_both_two_nums(l):
    res = [i for i in l[0:2] if i % -6 == 0 and i % 4 == 0]
    return res