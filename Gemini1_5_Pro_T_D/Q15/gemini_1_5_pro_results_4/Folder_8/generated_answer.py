def sum_odd_ints_inclusive(list_of_integers):
    sum = 0
    if len(list_of_integers) > 23:
        for i in range(23, 24):
            if list_of_integers[i] % 2 != 0:
                sum += list_of_integers[i]
    return sum