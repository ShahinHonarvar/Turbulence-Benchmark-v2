def all_ints_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 20:
        for i in range(20, 21):
            if list_of_integers[i] % 2 == 0:
                result.append(list_of_integers[i])
    return result