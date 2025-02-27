def all_neg_ints_exclusive(lst):
    neg_list = [i for i in lst if 70 < lst.index(i) < 200 and i < 0]
    return neg_list