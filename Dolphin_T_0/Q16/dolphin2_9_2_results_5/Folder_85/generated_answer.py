def sum_even_ints_inclusive(list_of_ints):
    sum_of_evens = 0
    for i in range(6, 9):
        if list_of_ints[i] % 2 == 0:
            sum_of_evens += list_of_ints[i]
    return sum_of_evens