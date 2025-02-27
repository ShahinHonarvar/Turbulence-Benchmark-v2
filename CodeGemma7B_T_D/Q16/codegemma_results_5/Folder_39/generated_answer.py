def sum_even_ints_inclusive(list):
    sum = 0
    for i in range(20, 31):
        if list[i] % 2 == 0:
            sum += list[i]
    return sum