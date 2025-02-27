def all_ints_div_by_both_two_nums(list_of_integers: list) -> list:
    result = []
    for i in range(0, 1):
        if i in range(len(list_of_integers)):
            the_int = list_of_integers[i]
            if the_int % 1 == 0 and the_int % -1 == 0:
                result.append(the_int)
    return result