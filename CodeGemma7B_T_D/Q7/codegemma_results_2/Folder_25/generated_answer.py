def all_even_ints_inclusive(integers):
    even_integers = []
    for integer in integers[29:94]:
        if integer % 2 == 0:
            even_integers.append(integer)
    return even_integers