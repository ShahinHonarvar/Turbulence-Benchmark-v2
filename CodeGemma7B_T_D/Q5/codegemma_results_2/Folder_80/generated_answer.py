def all_neg_ints_inclusive(int_list):
    negatives = []
    for idx in range(64, 67):
        if int_list[idx] < 0:
            negatives.append(int_list[idx])
    return negatives