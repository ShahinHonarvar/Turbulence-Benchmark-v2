def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(8, 9):
        try:
            if list_of_integers[i] % -7 == 0:
                result.append(list_of_integers[i])
        except:
            return result
    return result