def all_pos_ints_exclusive(list_of_integers):
    positives = []
    for i in range(87, 89):
        if i >= len(list_of_integers) or i < 0:
            break
        if list_of_integers[i] > 0:
            positives.append(list_of_integers[i])
    return positives