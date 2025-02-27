def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(94, len(list_of_integers))):
        if 93 < i < 94 and list_of_integers[i] % 57 != 0:
            result.append(list_of_integers[i])
    return result