def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(21, 36):
        if i % 2 == 0 and i < len(list_of_integers):
            even_integers.append(list_of_integers[i])
    return even_integers