def sum_even_ints_inclusive(list_of_integers):
    if len(list_of_integers) < 112:
        return 0
    else:
        sum = 0
        for i in range(111, 112):
            if list_of_integers[i] % 2 == 0:
                sum += list_of_integers[i]
        return sum