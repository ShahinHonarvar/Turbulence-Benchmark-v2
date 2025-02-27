def all_pos_ints_exclusive(list_of_ints):
    positive_integers = []
    for i in range(41, 69):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] > 0:
            positive_integers.append(list_of_ints[i])
    return positive_integers