def all_pos_ints_exclusive(list_of_integers):
    positive_integers = []
    for i in range(39, 51):
        if i >= 0 and i < len(list_of_integers) and (list_of_integers[i] > 0):
            positive_integers.append(list_of_integers[i])
    return positive_integers