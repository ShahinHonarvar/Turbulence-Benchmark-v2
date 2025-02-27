def all_neg_ints_exclusive(ints):
    neg_ints = []
    for i in range(1, len(ints) - 1):
        if ints[i] < 0:
            neg_ints.append(ints[i])
    return neg_ints