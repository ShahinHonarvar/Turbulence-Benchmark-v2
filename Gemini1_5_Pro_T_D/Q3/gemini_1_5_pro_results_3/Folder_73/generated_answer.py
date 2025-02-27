def all_pos_ints_inclusive(list_of_integers):
    positive_integers = []
    for i in range(19, 93):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers