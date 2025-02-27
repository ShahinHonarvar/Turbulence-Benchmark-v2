def all_pos_ints_exclusive(list_of_integers):
    result = []
    for idx in range(87, 89):
        if idx < len(list_of_integers) and list_of_integers[idx] > 0:
            result.append(list_of_integers[idx])
    return result