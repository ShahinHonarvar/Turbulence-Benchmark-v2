def all_even_ints_exclusive(list_of_integers):
    even_integers = []
    for i in range(21, 93):
        if i % 2 == 0 and i in list_of_integers:
            even_integers.append(i)
    return even_integers