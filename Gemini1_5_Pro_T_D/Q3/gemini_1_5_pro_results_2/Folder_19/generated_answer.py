def all_pos_ints_inclusive(list_of_integers):
    positives = []
    for i in range(3, 6):
        if i < len(list_of_integers) and list_of_integers[i] > 0:
            positives.append(list_of_integers[i])
    return positives