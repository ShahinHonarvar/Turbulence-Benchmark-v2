def all_neg_ints_exclusive(lst):
    negatives = []
    for i in range(8, 10):
        if lst[i] < 0:
            negatives.append(lst[i])
    return negatives