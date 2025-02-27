def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(0, 42), min(len(list_of_integers), 90)):
        if list_of_integers[i] % -59 == 0:
            result.append(list_of_integers[i])
    return result