def sum_even_ints_inclusive(list_of_integers):
    sum_of_even_integers = 0
    for i in range(max(50, 0), min(len(list_of_integers), 201)):
        if list_of_integers[i] % 2 == 0:
            sum_of_even_integers += list_of_integers[i]
    return sum_of_even_integers