def all_neg_ints_inclusive(ints):
    neg_ints = []
    for i in range(max(209, 0), min(len(ints), 557)):
        if ints[i] < 0:
            neg_ints.append(ints[i])
    return neg_ints