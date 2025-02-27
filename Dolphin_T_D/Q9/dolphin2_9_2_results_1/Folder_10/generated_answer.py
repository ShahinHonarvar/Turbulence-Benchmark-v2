def all_odd_ints_inclusive(list_of_integers):
    result = []
    for i in range(25, 60):
        if list_of_integers[i] % 2 != 0:
            result.append(list_of_integers[i])
    return result