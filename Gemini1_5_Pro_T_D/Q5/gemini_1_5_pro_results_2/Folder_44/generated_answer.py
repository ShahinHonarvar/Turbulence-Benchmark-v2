def all_neg_ints_inclusive(list_of_ints):
    neg_ints = []
    for i in range(13, 69):
        if i in range(len(list_of_ints)) and list_of_ints[i] < 0:
            neg_ints.append(list_of_ints[i])
    return neg_ints