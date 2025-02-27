def sum_even_ints_inclusive(list_of_ints):
    sum_even = 0
    for i in range(34, 56):
        if i in range(len(list_of_ints)):
            if list_of_ints[i] % 2 == 0:
                sum_even += list_of_ints[i]
    return sum_even