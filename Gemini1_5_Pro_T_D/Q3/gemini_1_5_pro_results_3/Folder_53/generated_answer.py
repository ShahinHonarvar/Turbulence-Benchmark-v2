def all_pos_ints_inclusive(list_of_integers):
    return [list_of_integers[i] for i in range(100, 201) if i < len(list_of_integers) and list_of_integers[i] > 0]