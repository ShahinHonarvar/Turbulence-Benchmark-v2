def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(12, 0), min(78, len(list_of_integers))):
        if list_of_integers[i] % -19 == 0:
            result.append(list_of_integers[i])
    return result