def all_neg_ints_exclusive(list_of_integers):
    negative_integers = []
    for i in range(len(list_of_integers)):
        if i > 3 and i < 5 and (list_of_integers[i] < 0):
            negative_integers.append(list_of_integers[i])
    return negative_integers