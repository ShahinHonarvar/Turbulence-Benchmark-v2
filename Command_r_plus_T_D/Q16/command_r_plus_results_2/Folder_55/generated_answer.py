def sum_even_ints_inclusive(numbers_list):
    even_sum = 0
    for index, num in enumerate(numbers_list[:11]):
        if num % 2 == 0:
            even_sum += num
    return even_sum