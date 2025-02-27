def all_neg_ints_inclusive(lst):
    neg_lst = [i for i in lst[3:6] if i < 0]
    if len(neg_lst) > 0:
        return neg_lst
    return []