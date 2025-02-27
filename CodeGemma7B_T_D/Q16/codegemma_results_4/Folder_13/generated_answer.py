def sum_even_ints_inclusive(list_of_ints):
    total_sum = 0
    for index in range(25, 88):
        if list_of_ints[index] % 2 == 0:
            total_sum += list_of_ints[index]
    return total_sum or 0