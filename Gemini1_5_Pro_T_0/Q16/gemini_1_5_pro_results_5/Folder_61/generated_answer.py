def sum_even_ints_inclusive(list_of_integers):
    sum = 0
    for i in range(min(8, len(list_of_integers))):
        if list_of_integers[i] % 2 == 0:
            sum += list_of_integers[i]
    return sum