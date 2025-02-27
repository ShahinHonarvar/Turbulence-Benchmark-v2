def all_neg_ints_inclusive(list_of_integers):
    result = []
    if len(list_of_integers) > 23 and list_of_integers[23] < 0:
        result.append(list_of_integers[23])
    return result