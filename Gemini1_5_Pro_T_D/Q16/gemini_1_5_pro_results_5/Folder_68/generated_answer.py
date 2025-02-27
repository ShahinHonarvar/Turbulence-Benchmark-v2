def sum_even_ints_inclusive(list_of_ints):
    sum_even = 0
    for i in range(min(9, len(list_of_ints))):
        if list_of_ints[i] % 2 == 0:
            sum_even += list_of_ints[i]
    return sum_even