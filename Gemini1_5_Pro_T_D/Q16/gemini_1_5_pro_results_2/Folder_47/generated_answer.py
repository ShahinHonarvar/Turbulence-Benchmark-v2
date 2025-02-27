def sum_even_ints_inclusive(list_of_integers):
    sum_of_evens = 0
    for i in range(37, 77):
        if i in range(len(list_of_integers)):
            if list_of_integers[i] % 2 == 0:
                sum_of_evens += list_of_integers[i]
    return sum_of_evens