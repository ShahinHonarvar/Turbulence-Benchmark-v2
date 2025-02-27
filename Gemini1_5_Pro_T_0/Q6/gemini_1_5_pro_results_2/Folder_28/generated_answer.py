def all_neg_ints_exclusive(list_of_integers):
    result = []
    for i in range(21, 51):
        if i < len(list_of_integers) and list_of_integers[i] < 0:
            result.append(list_of_integers[i])
    return result