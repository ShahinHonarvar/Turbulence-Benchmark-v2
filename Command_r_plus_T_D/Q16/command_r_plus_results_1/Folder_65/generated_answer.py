def sum_even_ints_inclusive(numbers_list):
    total = 0
    for i in range(56, 99):
        if numbers_list[i] % 2 == 0:
            total += numbers_list[i]
    return total