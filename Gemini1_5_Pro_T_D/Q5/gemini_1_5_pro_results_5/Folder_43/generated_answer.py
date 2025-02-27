def all_neg_ints_inclusive(list1):
    neg_ints = []
    for i in range(68, 87):
        if i in range(len(list1)):
            if list1[i] < 0:
                neg_ints.append(list1[i])
    return neg_ints