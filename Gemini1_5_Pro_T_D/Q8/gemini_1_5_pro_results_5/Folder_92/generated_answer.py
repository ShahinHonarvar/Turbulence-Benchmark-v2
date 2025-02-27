def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers