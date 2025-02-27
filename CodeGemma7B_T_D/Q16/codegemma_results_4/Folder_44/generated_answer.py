def sum_even_ints_inclusive(list_of_ints):
    sum_of_even_ints = 0
    for i in range(13, 69):
        if list_of_ints[i] % 2 == 0:
            sum_of_even_ints += list_of_ints[i]
    return sum_of_even_ints or 0