def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(43, 0), min(77, len(list_of_integers))):
        if list_of_integers[i] % 14 == 0:
            result.append(list_of_integers[i])
    return result