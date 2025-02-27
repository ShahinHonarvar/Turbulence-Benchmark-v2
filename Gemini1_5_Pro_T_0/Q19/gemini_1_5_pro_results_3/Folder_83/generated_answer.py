def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(90, 0), min(200, len(list_of_integers))):
        if list_of_integers[i] % -31 != 0:
            result.append(list_of_integers[i])
    return result