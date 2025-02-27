def sum_even_ints_inclusive(numbers_list):
    total_sum = 0
    for index, number in enumerate(numbers_list[:9]):
        if number % 2 == 0:
            total_sum += number
    return total_sum