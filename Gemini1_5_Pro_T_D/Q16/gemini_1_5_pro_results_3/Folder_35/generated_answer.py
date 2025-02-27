def sum_even_ints_inclusive(list_of_ints):
    sum = 0
    for i in range(30, 49):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 2 == 0:
            sum += list_of_ints[i]
    return sum