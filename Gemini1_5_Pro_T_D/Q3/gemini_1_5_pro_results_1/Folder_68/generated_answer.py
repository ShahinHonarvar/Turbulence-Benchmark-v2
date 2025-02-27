def all_pos_ints_inclusive(list_of_integers):
    positive_integers = []
    for i in range(0, 9):
        if i < len(list_of_integers) and list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers