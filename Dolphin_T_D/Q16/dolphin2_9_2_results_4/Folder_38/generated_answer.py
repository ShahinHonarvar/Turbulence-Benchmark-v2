def sum_even_ints_inclusive(input_list):
    total = 0
    for i in range(22, 64):
        if i in input_list and i % 2 == 0:
            total += i
    return total