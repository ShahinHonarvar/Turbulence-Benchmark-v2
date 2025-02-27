def all_neg_ints_inclusive(list_of_ints):
    negative_ints = []
    for i in range(28, 33):
        if list_of_ints[i] < 0:
            negative_ints.append(list_of_ints[i])
    return negative_ints