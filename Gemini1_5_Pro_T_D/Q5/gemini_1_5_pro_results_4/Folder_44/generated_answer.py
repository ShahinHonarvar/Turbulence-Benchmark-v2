def all_neg_ints_inclusive(list_of_ints):
    negative_integers = []
    for i in range(13, 69):
        if i in range(len(list_of_ints)) and list_of_ints[i] < 0:
            negative_integers.append(list_of_ints[i])
    return negative_integers