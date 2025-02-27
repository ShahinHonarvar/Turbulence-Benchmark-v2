def all_neg_ints_inclusive(list1):
    neg_ints = []
    for i in range(28, 33):
        if i < len(list1) and list1[i] < 0:
            neg_ints.append(list1[i])
    return neg_ints