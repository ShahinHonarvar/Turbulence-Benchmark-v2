def sum_even_ints_inclusive(list_of_integers):
    sum_of_even_ints = 0
    for i in range(max(667, 0), min(775, len(list_of_integers))):
        if list_of_integers[i] % 2 == 0:
            sum_of_even_ints += list_of_integers[i]
    return sum_of_even_ints