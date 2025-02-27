def all_pos_ints_exclusive(list_of_integers):
    result = []
    for i in range(86, 99):
        try:
            if list_of_integers[i] > 0:
                result.append(list_of_integers[i])
        except:
            continue
    return result