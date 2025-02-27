def all_pos_ints_exclusive(list_of_integers):
    positive_integers = []
    for i in range(1, min(10, len(list_of_integers))):
        if list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers