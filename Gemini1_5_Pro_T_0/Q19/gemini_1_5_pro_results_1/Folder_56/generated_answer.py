def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) < 10:
        return result
    for i in range(7, 9):
        if list_of_integers[i] % -9 != 0:
            result.append(list_of_integers[i])
    return result