def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(max(69, 0), min(98, len(list_of_integers))):
        if list_of_integers[i] % -90 == 0 and list_of_integers[i] % -67 == 0:
            result.append(list_of_integers[i])
    return result