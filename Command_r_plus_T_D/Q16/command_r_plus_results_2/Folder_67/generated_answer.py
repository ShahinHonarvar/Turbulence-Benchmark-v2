def sum_even_ints_inclusive(numbers_list):
    sum_even_numbers = 0
    for i in range(22, 51):
        if numbers_list[i] % 2 == 0:
            sum_even_numbers += numbers_list[i]
    return sum_even_numbers