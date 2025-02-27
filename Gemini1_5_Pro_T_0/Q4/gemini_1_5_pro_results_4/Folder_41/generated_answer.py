def all_pos_ints_exclusive(list_of_integers):
    positive_integers = []
    for i in range(9, 10):
        if 8 <= i < 9 and list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers