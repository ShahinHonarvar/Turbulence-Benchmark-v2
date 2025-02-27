def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(0, min(len(list_of_integers) - 1, 70))):
        if i < 13:
            continue
        if list_of_integers[i] % -78 != 0:
            result.append(list_of_integers[i])
    return result