def all_pos_ints_exclusive(list_of_integers):
    positives = []
    for i in range(29, 49):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] > 0:
            positives.append(list_of_integers[i])
    return positives