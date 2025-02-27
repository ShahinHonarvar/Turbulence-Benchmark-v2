def all_neg_ints_inclusive(list_of_integers):
    negative_integers = []
    if len(list_of_integers) > 0:
        if list_of_integers[0] < 0:
            negative_integers.append(list_of_integers[0])
    return negative_integers