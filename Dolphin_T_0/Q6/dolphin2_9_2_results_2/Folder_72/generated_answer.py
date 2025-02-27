def all_neg_ints_exclusive(lst):
    neg_lst = []
    for i in range(56, 88):
        if lst[i] < 0:
            neg_lst.append(lst[i])
    return neg_lst