def all_neg_ints_exclusive(lst):
    lst2 = []
    for i in range(49, 74):
        if lst[i] < 0:
            lst2.append(lst[i])
    return lst2