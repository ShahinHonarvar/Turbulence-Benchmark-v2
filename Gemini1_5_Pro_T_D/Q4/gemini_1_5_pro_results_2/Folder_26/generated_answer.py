def all_pos_ints_exclusive(list_of_integers):
    positive_integers = []
    for i in range(44, 78):
        if i in range(len(list_of_integers)) and list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers