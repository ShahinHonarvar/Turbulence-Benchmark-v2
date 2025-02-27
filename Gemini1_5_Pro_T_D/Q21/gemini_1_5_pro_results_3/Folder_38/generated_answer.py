def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(12, len(list_of_integers)), min(15, len(list_of_integers)) + 1):
        if list_of_integers[i] % -80 == 0:
            result.append(list_of_integers[i])
    return result