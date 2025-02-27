def all_ints_div_by_both_two_nums(list_of_integers):
    result = []
    for i in range(20, 94):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % -92 == 0 and list_of_integers[i] % -50 == 0:
            result.append(list_of_integers[i])
    return result