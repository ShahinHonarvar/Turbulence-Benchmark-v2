def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(58, 76):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 72 == 0 and list_of_integers[i] % 62 == 0:
            result.append(list_of_integers[i])
    return result