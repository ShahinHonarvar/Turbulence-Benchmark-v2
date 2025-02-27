def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    for i in range(min(5, len(list_of_integers))):
        if list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers