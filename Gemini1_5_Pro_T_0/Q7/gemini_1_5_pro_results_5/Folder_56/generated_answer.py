def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    if list_of_integers:
        if list_of_integers[0] % 2 == 0:
            even_integers.append(list_of_integers[0])
    return even_integers