def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(57, 0), min(68, len(list_of_integers))):
        if list_of_integers[i] % 90 == 0:
            result.append(list_of_integers[i])
    return result