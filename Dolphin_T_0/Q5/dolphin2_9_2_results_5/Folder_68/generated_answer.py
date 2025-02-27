def all_neg_ints_inclusive(lst):
    negatives = []
    for i in range(9):
        if lst[i] < 0:
            negatives.append(lst[i])
    return negatives