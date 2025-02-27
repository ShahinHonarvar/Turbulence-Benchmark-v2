def all_neg_ints_inclusive(list_of_integers):
    negative_integers = []
    for i in range(min(len(list_of_integers), 10)):
        if list_of_integers[i] < 0:
            negative_integers.append(list_of_integers[i])
    return negative_integers