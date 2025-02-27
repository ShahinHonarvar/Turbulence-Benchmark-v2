def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(min(6, len(list_of_integers))):
        if list_of_integers[i] % 6 == 0:
            result.append(list_of_integers[i])
    return result