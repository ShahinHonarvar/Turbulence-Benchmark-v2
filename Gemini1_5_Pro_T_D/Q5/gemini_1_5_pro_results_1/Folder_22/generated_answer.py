def all_neg_ints_inclusive(ints):
    neg_ints = []
    for i in range(40, 201):
        if i < len(ints) and ints[i] < 0:
            neg_ints.append(ints[i])
    return neg_ints