def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(max(8, 0), min(9, len(list_of_integers))):
        if list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers