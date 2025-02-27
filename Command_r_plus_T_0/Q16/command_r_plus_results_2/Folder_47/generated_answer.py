def sum_even_ints_inclusive(numbers_list):
    even_sum = 0
    for index in range(37, 77):
        if numbers_list[index] % 2 == 0:
            even_sum += numbers_list[index]
    return even_sum