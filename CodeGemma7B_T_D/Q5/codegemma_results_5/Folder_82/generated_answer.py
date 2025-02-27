def all_neg_ints_inclusive(lst):
    return [i for i in lst if i < 0 and 20 <= lst.index(i) <= 200]