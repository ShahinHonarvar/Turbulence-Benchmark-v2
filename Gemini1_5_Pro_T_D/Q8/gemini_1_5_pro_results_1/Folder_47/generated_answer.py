def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(64, 80):
        if i < len(list_of_integers) and list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers