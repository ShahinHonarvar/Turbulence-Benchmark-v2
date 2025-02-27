def all_neg_ints_inclusive(list_of_ints):
    negative_ints = []
    for i in range(1, 6):
        if i < len(list_of_ints) and list_of_ints[i] < 0:
            negative_ints.append(list_of_ints[i])
    return negative_ints