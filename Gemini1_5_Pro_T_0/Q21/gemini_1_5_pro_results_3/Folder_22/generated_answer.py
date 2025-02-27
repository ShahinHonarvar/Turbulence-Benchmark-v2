def all_ints_div_by_num(list_of_integers):
    try:
        result = []
        for i in range(10, 11):
            if list_of_integers[i] % 1 == 0:
                result.append(list_of_integers[i])
        return result
    except IndexError:
        return []