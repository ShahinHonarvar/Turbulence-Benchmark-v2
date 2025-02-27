def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(10, 0), min(len(list_of_integers), 53)):
        if list_of_integers[i] % -12 == 0:
            result.append(list_of_integers[i])
    return result