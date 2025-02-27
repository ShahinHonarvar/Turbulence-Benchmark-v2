def all_pos_ints_inclusive(list_of_integers):
    positive_integers = []
    for i in range(max(62, 0), min(len(list_of_integers), 93)):
        if list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers