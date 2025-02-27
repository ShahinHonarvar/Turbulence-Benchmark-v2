def all_pos_ints_inclusive(list_of_integers):
    positive_integers = []
    for i in range(max(66, 0), min(len(list_of_integers), 94)):
        if list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers