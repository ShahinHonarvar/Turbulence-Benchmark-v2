def all_pos_ints_inclusive(list_of_integers):
    positive_integers = []
    for i in range(66, 94):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] > 0:
                positive_integers.append(list_of_integers[i])
    return positive_integers