def sum_even_ints_inclusive(list_of_ints):
    sum = 0
    for i in range(42, 69):
        if i in range(len(list_of_ints)) and list_of_ints[i] % 2 == 0:
            sum += list_of_ints[i]
    return sum