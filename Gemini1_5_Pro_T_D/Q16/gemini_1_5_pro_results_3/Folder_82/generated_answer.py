def sum_even_ints_inclusive(list_of_integers):
    sum = 0
    if len(list_of_integers) > 29:
        if list_of_integers[29] % 2 == 0:
            sum += list_of_integers[29]
    return sum