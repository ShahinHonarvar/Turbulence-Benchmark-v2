def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    for i in range(28, 41):
        if i < len(list_of_integers) and list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers