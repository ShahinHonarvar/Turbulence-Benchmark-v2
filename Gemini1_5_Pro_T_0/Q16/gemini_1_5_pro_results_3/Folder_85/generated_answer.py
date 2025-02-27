def sum_even_ints_inclusive(list_of_integers):
    sum_of_even_integers = 0
    for i in range(6, 9):
        if i < len(list_of_integers):
            if list_of_integers[i] % 2 == 0:
                sum_of_even_integers += list_of_integers[i]
    return sum_of_even_integers