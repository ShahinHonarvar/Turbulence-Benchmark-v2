def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(31, 73):
        if i < len(list_of_integers) and list_of_integers[i] % -63 == 0:
            result.append(list_of_integers[i])
    return result