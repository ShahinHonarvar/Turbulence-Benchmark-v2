def sum_even_ints_inclusive(list_of_ints):
    total = 0
    for i in range(31, 73):
        if i < len(list_of_ints):
            if list_of_ints[i] % 2 == 0:
                total += list_of_ints[i]
    return total