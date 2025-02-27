def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(min(len(list_of_integers), 3)):
        if list_of_integers[i] % 3 == 0:
            result.append(list_of_integers[i])
    return result