def all_ints_not_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 200:
        for i in range(199, 201):
            if i < len(list_of_integers) and list_of_integers[i] % -200 != 0:
                result.append(list_of_integers[i])
    return result