def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for number in list_of_integers[86:90]:
        if number % -61 == 0 and number % -79 == 0:
            result.append(number)
    return result