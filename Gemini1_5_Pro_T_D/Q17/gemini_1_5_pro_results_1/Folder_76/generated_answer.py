def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(250, 630):
        if i in list_of_integers and i % 850 == 0 and (i % 587 == 0):
            result.append(i)
    return result