def all_pos_ints_inclusive(list_of_integers):
    result = []
    for index, value in enumerate(list_of_integers):
        if 28 <= index <= 38:
            if value > 0:
                result.append(value)
    return result