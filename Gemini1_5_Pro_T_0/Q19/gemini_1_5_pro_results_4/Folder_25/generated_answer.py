def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(29, 0), min(53, len(list_of_integers))):
        if list_of_integers[i] % -68 != 0:
            result.append(list_of_integers[i])
    return result