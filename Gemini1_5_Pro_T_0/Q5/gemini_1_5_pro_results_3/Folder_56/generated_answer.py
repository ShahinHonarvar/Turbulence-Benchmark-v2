def all_neg_ints_inclusive(list_of_ints):
    neg_ints = []
    if len(list_of_ints) > 0 and list_of_ints[0] < 0:
        neg_ints.append(list_of_ints[0])
    return neg_ints