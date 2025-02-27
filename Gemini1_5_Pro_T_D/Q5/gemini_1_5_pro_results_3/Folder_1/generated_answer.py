def all_neg_ints_inclusive(ints):
    neg_ints = []
    for i in range(31, 73):
        if i in range(len(ints)) and ints[i] < 0:
            neg_ints.append(ints[i])
    return neg_ints