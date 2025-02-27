def all_neg_ints_exclusive(list_of_ints):
    neg_ints = []
    for i in range(51, 199):
        if i in range(len(list_of_ints)):
            if list_of_ints[i] < 0:
                neg_ints.append(list_of_ints[i])
    return neg_ints