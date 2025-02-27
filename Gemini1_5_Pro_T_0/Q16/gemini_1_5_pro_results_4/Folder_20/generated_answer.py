def sum_even_ints_inclusive(list_of_ints):
    sum_of_even_ints = 0
    for i in range(56, 67):
        if i in range(len(list_of_ints)):
            if list_of_ints[i] % 2 == 0:
                sum_of_even_ints += list_of_ints[i]
    return sum_of_even_ints