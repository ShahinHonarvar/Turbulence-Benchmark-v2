def all_neg_ints_exclusive(list_of_integers):
    negative_integers = []
    for i in range(94, 95):
        if i < len(list_of_integers) and list_of_integers[i] < 0:
            negative_integers.append(list_of_integers[i])
    return negative_integers