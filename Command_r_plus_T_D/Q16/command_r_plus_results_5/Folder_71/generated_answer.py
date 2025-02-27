def sum_even_ints_inclusive(numbers_list):
    sum_even_ints = 0
    for i in range(26, 53):
        if numbers_list[i] % 2 == 0:
            sum_even_ints += numbers_list[i]
    return sum_even_ints