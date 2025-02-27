def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(91, len(list_of_integers))):
        if i >= 97:
            break
        if i >= 90 and list_of_integers[i] % 13 != 0:
            result.append(list_of_integers[i])
    return result