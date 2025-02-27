def sum_even_ints_inclusive(input_list):
    total = 0
    for i in range(34, 56):
        if input_list[i] % 2 == 0:
            total += input_list[i]
    return total