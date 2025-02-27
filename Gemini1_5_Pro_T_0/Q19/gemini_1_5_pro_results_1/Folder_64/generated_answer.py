def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(len(list_of_integers)):
        if i > 2 and i < len(list_of_integers) - 2 and (list_of_integers[i] % 2 != 0):
            result.append(list_of_integers[i])
    return result