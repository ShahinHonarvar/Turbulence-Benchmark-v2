def all_pos_ints_exclusive(list_of_integers):
    result = []
    for i in range(296, 573):
        if i in range(len(list_of_integers)) and list_of_integers[i] > 0:
            result.append(list_of_integers[i])
    return result