def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_numbers = 0
    for i in range(max(13, 0), min(92, len(list_of_integers))):
        if list_of_integers[i] % -65 == 0 or list_of_integers[i] % -62 == 0:
            sum_of_numbers += list_of_integers[i]
    return sum_of_numbers