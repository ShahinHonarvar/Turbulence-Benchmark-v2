def sum_odd_ints_inclusive(list_of_integers):
    sum = 0
    if len(list_of_integers) > 1:
        if list_of_integers[1] % 2 != 0:
            sum += list_of_integers[1]
    return sum