def all_ints_div_by_num(list_of_integers):
    result = []
    for i in range(max(0, 43), min(len(list_of_integers), 77)):
        if list_of_integers[i] % 14 == 0:
            result.append(list_of_integers[i])
    return result