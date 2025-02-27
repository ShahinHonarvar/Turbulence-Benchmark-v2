def all_even_ints_inclusive(list_of_integers):
    even_integers = []
    if len(list_of_integers) > 23:
        for integer in list_of_integers[23:24]:
            if integer % 2 == 0:
                even_integers.append(integer)
    return even_integers