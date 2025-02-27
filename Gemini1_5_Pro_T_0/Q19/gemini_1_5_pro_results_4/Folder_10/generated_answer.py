def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(87, len(list_of_integers))):
        if 86 < i < 89 and list_of_integers[i] % -61 != 0:
            result.append(list_of_integers[i])
    return result