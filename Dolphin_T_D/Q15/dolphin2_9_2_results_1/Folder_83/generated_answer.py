def sum_odd_ints_inclusive(list_of_ints):
    the_sum = 0
    for i in range(90, 201):
        if list_of_ints[i] % 2 != 0:
            the_sum += list_of_ints[i]
    return the_sum