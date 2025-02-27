def all_neg_ints_inclusive(lst):
    neg_lst = []
    for i in lst[56:99]:
        if i < 0:
            neg_lst.append(i)
    if len(neg_lst) == 0:
        return []
    return neg_lst