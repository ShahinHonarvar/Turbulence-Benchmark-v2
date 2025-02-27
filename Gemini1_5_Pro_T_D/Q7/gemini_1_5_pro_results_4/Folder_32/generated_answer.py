def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    if len(list_of_integers) < 98:
        return even_integers
    for i in range(21, 98):
        if list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers