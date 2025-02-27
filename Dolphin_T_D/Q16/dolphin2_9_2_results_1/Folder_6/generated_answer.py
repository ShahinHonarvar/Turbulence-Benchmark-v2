def sum_even_ints_inclusive(list_ints):
    sum = 0
    for i in range(10, 67):
        if i < len(list_ints) and list_ints[i] % 2 == 0:
            sum += list_ints[i]
    return sum