def all_neg_ints_inclusive(lst):
    neg_list = []
    for i in range(75, 89):
        if lst[i] < 0:
            neg_list.append(lst[i])
    return neg_list