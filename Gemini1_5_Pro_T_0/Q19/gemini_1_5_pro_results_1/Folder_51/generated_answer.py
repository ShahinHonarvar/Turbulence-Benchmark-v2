def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(1, len(list_of_integers))):
        if i > 1 and i < 6 and (list_of_integers[i] % 2 != 0):
            result.append(list_of_integers[i])
    return result