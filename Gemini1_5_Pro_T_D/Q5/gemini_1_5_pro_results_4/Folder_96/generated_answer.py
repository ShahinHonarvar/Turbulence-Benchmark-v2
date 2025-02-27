def all_neg_ints_inclusive(ints):
    neg_ints = []
    for i in range(50, 201):
        if i in range(len(ints)):
            if ints[i] < 0:
                neg_ints.append(ints[i])
    return neg_ints