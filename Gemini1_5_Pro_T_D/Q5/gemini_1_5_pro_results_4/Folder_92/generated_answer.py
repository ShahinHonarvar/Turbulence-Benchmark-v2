def all_neg_ints_inclusive(list_of_integers):
    result = []
    for i in range(min(len(list_of_integers), 2)):
        if list_of_integers[i] < 0:
            result.append(list_of_integers[i])
    return result