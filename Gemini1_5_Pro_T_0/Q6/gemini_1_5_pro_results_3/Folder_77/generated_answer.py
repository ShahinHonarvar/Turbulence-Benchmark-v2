def all_neg_ints_exclusive(ints):
    neg_ints = []
    for i in range(max(112, 0), min(473, len(ints))):
        if ints[i] < 0:
            neg_ints.append(ints[i])
    return neg_ints