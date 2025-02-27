def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(0, min(len(list_of_integers) - 1, 43)), min(len(list_of_integers), 77)):
        if list_of_integers[i] % 84 != 0:
            result.append(list_of_integers[i])
    return result