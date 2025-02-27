def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(8, 0), min(len(list_of_integers), 9)):
        if list_of_integers[i] % -3 != 0:
            result.append(list_of_integers[i])
    return result