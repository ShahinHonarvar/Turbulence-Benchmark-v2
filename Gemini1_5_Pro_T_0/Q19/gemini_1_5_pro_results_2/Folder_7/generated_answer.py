def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(496, 0), min(len(list_of_integers), 826)):
        if list_of_integers[i] % -201 != 0:
            result.append(list_of_integers[i])
    return result