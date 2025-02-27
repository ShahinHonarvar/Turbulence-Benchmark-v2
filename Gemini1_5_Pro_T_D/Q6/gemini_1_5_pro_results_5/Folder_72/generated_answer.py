def all_neg_ints_exclusive(list1):
    neg_ints = []
    for i in range(57, 88):
        if i < len(list1) and list1[i] < 0:
            neg_ints.append(list1[i])
    return neg_ints