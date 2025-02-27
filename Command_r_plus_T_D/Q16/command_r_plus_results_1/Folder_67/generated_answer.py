def sum_even_ints_inclusive(numbers_list):
    sum_even_ints = 0
    for index in range(22, 51):
        if numbers_list[index] % 2 == 0:
            sum_even_ints += numbers_list[index]
    return sum_even_ints