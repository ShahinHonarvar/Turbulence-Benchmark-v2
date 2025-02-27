def all_neg_ints_exclusive(lst):
    result = [i for i in lst if 3 < lst.index(i) < 8 and i < 0]
    return result