def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    if len(list_of_integers) > 6:
        for i in range(6, 7):
            if list_of_integers[i] % 2 == 0:
                even_integers.append(list_of_integers[i])
        return even_integers
    else:
        return even_integers