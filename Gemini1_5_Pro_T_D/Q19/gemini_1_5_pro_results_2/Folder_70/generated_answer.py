def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 97:
        for i in range(91, 97):
            if list_of_integers[i] % 13 != 0:
                result.append(list_of_integers[i])
    return result