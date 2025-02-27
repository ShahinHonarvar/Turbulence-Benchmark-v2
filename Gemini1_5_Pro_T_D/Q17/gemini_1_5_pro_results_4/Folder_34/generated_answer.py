def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(max(60, 0), min(len(list_of_integers), 201)):
        if list_of_integers[i] % 9 == 0 and list_of_integers[i] % 11 == 0:
            result.append(list_of_integers[i])
    return result