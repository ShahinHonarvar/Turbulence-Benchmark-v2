def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for num in list_of_integers[29:54]:
        if num % -68 == 0 and num % -85 == 0:
            result.append(num)
    return result