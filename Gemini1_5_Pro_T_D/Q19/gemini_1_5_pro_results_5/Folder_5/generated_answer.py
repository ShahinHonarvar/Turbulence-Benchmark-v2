def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(len(list_of_integers)):
        if i > 0 and i < len(list_of_integers) - 1 and (list_of_integers[i] % 8 != 0):
            result.append(list_of_integers[i])
    return result