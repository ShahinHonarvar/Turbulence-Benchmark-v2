def all_neg_ints_exclusive(lst):
    neg_lst = []
    for i in range(94, 93, -1):
        if lst[i] < 0:
            neg_lst.append(lst[i])
    return neg_lst