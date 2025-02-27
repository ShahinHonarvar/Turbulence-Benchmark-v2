def all_neg_ints_inclusive(list_of_ints):
    neg_ints = []
    for i in range(min(len(list_of_ints), 8)):
        if list_of_ints[i] < 0:
            neg_ints.append(list_of_ints[i])
    return neg_ints