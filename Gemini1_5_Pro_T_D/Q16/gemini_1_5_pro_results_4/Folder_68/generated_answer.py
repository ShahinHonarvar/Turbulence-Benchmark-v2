def sum_even_ints_inclusive(list_of_ints):
    sum = 0
    for i in range(min(9, len(list_of_ints))):
        if list_of_ints[i] % 2 == 0:
            sum += list_of_ints[i]
    return sum