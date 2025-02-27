def sum_even_ints_inclusive(ints_list):
    sum = 0
    for i in range(1, 9):
        if bits_list[i] % 2 == 0:
            sum += ints_list[i]
    return sum