def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(87, 99):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers