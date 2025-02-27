def sum_even_ints_inclusive(numbers_list):
    sum_even = 0
    for i in range(91, 100):
        if numbers_list[i] % 2 == 0:
            sum_even += numbers_list[i]
    return sum_even