def all_neg_ints_exclusive(int_list):
    negatives = []
    for i in range(11, 76):
        if int_list[i] < 0:
            negatives.append(int_list[i])
    return negatives