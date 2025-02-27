def sum_even_ints_inclusive(list_of_ints):
    sum_of_numbers = 0
    for i in range(75, 86):
        if i in range(len(list_of_ints)):
            if list_of_ints[i] % 2 == 0:
                sum_of_numbers += list_of_ints[i]
    return sum_of_numbers