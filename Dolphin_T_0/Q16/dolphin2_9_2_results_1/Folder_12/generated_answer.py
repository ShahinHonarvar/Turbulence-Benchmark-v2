def sum_even_ints_inclusive(list_of_integers):
    total = 0
    for i in range(14, 65):
        if i < len(list_of_integers) and list_of_integers[i] % 2 == 0:
            total += list_of_integers[i]
    return total