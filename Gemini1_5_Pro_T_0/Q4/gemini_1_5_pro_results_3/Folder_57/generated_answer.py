def all_pos_ints_exclusive(list_of_integers):
    positive_integers = []
    for i in range(19, 37):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] > 0:
            positive_integers.append(list_of_integers[i])
    return positive_integers