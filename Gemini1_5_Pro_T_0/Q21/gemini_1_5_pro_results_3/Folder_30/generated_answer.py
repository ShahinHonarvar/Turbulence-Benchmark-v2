def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(0, 59), min(len(list_of_integers), 80)):
        if list_of_integers[i] % -82 == 0:
            result.append(list_of_integers[i])
    return result