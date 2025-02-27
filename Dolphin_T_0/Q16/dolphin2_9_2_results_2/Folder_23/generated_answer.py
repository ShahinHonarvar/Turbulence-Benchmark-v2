def sum_even_ints_inclusive(ints_list):
    total = 0
    for i in range(52, 72):
        if ints_list[i] % 2 == 0:
            total += ints_list[i]
    return total