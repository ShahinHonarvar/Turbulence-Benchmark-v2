def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(min(2, len(list_of_integers))):
        if list_of_integers[i] % -6 == 0 and list_of_integers[i] % 4 == 0:
            result.append(list_of_integers[i])
    return result