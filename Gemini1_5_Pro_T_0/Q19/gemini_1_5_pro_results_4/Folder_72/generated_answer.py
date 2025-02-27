def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(13, len(list_of_integers)) + 1, min(70, len(list_of_integers))):
        if list_of_integers[i] % -78 != 0:
            result.append(list_of_integers[i])
    return result