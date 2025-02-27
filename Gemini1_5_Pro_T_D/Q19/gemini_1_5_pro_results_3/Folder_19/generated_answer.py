def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 5:
        for i in range(4, 5):
            if list_of_integers[i] % -7 != 0:
                result.append(list_of_integers[i])
    return result