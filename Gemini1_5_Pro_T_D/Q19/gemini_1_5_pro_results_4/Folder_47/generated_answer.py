def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(26, 76):
        if i < len(list_of_integers) and list_of_integers[i] % -53 != 0:
            result.append(list_of_integers[i])
    return result