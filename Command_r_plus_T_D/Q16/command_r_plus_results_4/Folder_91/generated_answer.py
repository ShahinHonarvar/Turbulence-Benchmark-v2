def sum_even_ints_inclusive(numbers_list):
    even_sum = 0
    for i in range(6):
        if numbers_list[i] % 2 == 0:
            even_sum += numbers_list[i]
    return even_sum