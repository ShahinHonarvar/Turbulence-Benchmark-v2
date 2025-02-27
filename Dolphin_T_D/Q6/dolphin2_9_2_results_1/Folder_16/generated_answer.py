def all_neg_ints_exclusive(lst):
    negatives = []
    for i in range(87, 90):
        if lst[i] < 0:
            negatives.append(lst[i])
    return negatives