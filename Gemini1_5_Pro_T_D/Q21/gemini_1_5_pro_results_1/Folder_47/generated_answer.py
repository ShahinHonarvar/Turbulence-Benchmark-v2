def all_ints_div_by_num(list_of_integers: list) -> list:
    result = []
    for i in range(75, 89):
        try:
            if list_of_integers[i] % -27 == 0:
                result.append(list_of_integers[i])
        except:
            continue
    return result