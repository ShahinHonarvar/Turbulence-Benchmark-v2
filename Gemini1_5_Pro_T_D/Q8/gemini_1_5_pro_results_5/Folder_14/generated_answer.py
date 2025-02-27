def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(len(list_of_integers)):
        if i > 0 and i < 7 and (list_of_integers[i] % 2 == 0):
            even_integers.append(list_of_integers[i])
    return even_integers