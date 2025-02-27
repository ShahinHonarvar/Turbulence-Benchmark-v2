def all_neg_ints_exclusive(ints):
    return [ints[i] for i in range(1, len(ints) - 1) if ints[i] < 0]