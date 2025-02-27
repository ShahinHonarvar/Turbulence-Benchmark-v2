def all_neg_ints_inclusive(list_of_integers):
    negative_integers = []
    if len(list_of_integers) > 6:
        if list_of_integers[6] < 0:
            negative_integers.append(list_of_integers[6])
    return negative_integers