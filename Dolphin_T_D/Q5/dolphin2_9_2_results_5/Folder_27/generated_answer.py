def all_neg_ints_inclusive(lst):
    negative_lst = []
    for i in range(66, 94):
        if lst[i] < 0:
            negative_lst.append(lst[i])
    return negative_lst