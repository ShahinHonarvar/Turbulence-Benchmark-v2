def all_neg_ints_inclusive(lst):
    neg_lst = [i for i in lst[28:39] if i < 0]
    return neg_lst if len(neg_lst) > 0 else []