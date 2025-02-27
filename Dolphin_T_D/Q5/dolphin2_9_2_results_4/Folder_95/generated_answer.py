def all_neg_ints_inclusive(list_of_integers):
    negatives = []
    for i in range(82, 87):
        if list_of_integers[i] < 0:
            negatives.append(list_of_integers[i])
    return negatives