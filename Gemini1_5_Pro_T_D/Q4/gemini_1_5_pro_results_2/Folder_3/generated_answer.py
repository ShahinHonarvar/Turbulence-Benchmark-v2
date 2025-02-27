def all_pos_ints_exclusive(list_of_integers):
    positive_integers = []
    for i in range(79, 92):
        if list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers