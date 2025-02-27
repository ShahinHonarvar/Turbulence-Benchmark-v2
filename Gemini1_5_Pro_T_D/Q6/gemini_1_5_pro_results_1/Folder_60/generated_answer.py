def all_neg_ints_exclusive(list_of_integers):
    negative_integers = []
    for i in range(45, 91):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] < 0:
            negative_integers.append(list_of_integers[i])
    return negative_integers