def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    if len(list_of_integers) > 7:
        if list_of_integers[7] % 2 == 0:
            even_integers.append(list_of_integers[7])
    return even_integers