def all_neg_ints_exclusive(list_of_integers):
    negative_integers = []
    for i in range(max(2, len(list_of_integers))):
        if i >= 2 and i < min(7, len(list_of_integers)):
            if list_of_integers[i] < 0:
                negative_integers.append(list_of_integers[i])
    return negative_integers