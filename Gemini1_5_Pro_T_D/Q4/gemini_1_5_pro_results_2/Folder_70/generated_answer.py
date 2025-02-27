def all_pos_ints_exclusive(list_of_integers):
    new_list = []
    for i in range(38, 81):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] > 0:
            new_list.append(list_of_integers[i])
    return new_list