def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(41, 69):
        try:
            if list_of_integers[i] % -82 != 0:
                result.append(list_of_integers[i])
        except:
            continue
    return result