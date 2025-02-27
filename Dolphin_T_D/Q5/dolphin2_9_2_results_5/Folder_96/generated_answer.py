def all_neg_ints_inclusive(lst):
    neg_lst = [-1 * i for i in lst[49:200]]
    if all((i >= 0 for i in neg_lst)):
        return []
    else:
        return neg_lst