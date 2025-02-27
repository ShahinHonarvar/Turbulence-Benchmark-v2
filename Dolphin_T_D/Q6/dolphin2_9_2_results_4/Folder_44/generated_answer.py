def all_neg_ints_exclusive(lst):
    neg_lst = []
    for i in range(81, 86):
        if lst[i] < 0:
            neg_lst.append(lst[i])
    return neg_lst