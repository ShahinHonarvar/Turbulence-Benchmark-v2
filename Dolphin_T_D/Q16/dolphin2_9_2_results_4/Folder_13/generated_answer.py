def sum_even_ints_inclusive(list_of_integers):
    total = 0
    for i in range(25, 88):
        if list_of_integers[i] % 2 == 0:
            total += list_of_integers[i]
    return total