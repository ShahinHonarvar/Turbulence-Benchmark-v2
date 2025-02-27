def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(87, len(list_of_integers) - 3), min(89, len(list_of_integers))):
        if list_of_integers[i] % -61 != 0:
            result.append(list_of_integers[i])
    return result