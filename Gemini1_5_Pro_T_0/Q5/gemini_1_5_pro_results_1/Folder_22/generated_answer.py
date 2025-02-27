def all_neg_ints_inclusive(list_of_integers):
    negative_integers = []
    for i in range(40, 201):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] < 0:
            negative_integers.append(list_of_integers[i])
    return negative_integers