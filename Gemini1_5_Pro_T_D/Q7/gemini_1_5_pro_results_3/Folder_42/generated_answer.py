def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    for index in range(29, 80):
        if index in range(len(list_of_integers)):
            if list_of_integers[index] % 2 == 0:
                even_integers.append(list_of_integers[index])
    return even_integers