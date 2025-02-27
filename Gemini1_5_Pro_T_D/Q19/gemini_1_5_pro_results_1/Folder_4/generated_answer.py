def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(19, 0), min(len(list_of_integers), 49)):
        if list_of_integers[i] % -36 != 0:
            result.append(list_of_integers[i])
    return result