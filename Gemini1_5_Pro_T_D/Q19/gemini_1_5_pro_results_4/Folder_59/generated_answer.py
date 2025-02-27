def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(8, len(list_of_integers))):
        if i >= 9:
            break
        if list_of_integers[i] % 8 != 0:
            result.append(list_of_integers[i])
    return result