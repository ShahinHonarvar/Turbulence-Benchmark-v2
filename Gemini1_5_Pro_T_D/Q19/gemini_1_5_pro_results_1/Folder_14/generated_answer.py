def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(2, len(list_of_integers) - 2)):
        if i >= 2 and i < 7 and (list_of_integers[i] % 8 != 0):
            result.append(list_of_integers[i])
    return result