def all_pos_ints_inclusive(list_of_integers):
    positive_integers = []
    for i in range(14, 65):
        if i - 1 < len(list_of_integers) and list_of_integers[i - 1] > 0:
            positive_integers.append(list_of_integers[i - 1])
    return positive_integers