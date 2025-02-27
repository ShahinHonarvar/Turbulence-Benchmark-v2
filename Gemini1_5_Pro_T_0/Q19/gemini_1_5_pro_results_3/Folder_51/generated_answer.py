def all_ints_not_div_by_num(list_of_integers):
    result = []
    for i in range(max(1, len(list_of_integers) - 5)):
        if i + 1 >= len(list_of_integers) or i + 1 <= 1:
            continue
        if list_of_integers[i + 1] % 2 != 0:
            result.append(list_of_integers[i + 1])
    return result