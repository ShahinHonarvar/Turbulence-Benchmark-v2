def sum_even_ints_inclusive(list):
    sum_of_even_ints = 0
    for i in range(90, 201):
        if list[i] % 2 == 0:
            sum_of_even_ints += list[i]
    return sum_of_even_ints