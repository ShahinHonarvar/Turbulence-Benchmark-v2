def all_neg_ints_exclusive(lst):
    neg_ints = []
    for i in range(len(lst)):
        if i > 1 and i < 7 and (lst[i] < 0):
            neg_ints.append(lst[i])
    return neg_ints