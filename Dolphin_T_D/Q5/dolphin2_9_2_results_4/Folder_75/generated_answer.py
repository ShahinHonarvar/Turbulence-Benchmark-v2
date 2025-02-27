def all_neg_ints_inclusive(lst):
    neg_list = []
    for i in range(56, 58):
        if lst[i] < 0:
            neg_list.append(lst[i])
    return neg_list