def all_ints_div_by_num(list_of_integers):
    result = []
    if len(list_of_integers) > 0 and list_of_integers[0] % 5 == 0:
        result.append(list_of_integers[0])
    return result