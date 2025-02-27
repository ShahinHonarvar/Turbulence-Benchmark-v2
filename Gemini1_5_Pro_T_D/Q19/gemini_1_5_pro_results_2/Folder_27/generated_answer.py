def all_ints_not_div_by_num(list_of_integers):
    result = []
    if 21 <= len(list_of_integers) and 14 < 21:
        for i in range(14 + 1, 21):
            if list_of_integers[i] % -93 != 0:
                result.append(list_of_integers[i])
    return result