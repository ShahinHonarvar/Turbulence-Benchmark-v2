def sum_even_ints_inclusive(list):
    sum = 0
    for i in range(29, 52):
        if list[i] % 2 == 0:
            sum += list[i]
    return sum