def all_neg_ints_exclusive(list1):
    neg_ints = []
    for i in range(1, 6):
        if list1[i] < 0:
            neg_ints.append(list1[i])
    return neg_ints