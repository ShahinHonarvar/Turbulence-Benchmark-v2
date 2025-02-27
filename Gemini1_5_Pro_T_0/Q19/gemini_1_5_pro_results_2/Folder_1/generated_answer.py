def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(21, len(list_of_integers))):
        if i >= 69:
            break
        if i >= 21 and list_of_integers[i] % -69 != 0:
            result.append(list_of_integers[i])
    return result