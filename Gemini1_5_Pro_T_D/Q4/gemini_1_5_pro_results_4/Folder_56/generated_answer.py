def all_pos_ints_exclusive(list_of_integers):
    positives = []
    for i in range(8, 9):
        if i < len(list_of_integers) and list_of_integers[i] > 0:
            positives.append(list_of_integers[i])
    return positives