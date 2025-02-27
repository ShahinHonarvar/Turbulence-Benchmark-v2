def sum_even_ints_inclusive(numbers_list):
    total_sum = 0
    for num in numbers_list:
        if num % 2 == 0:
            total_sum += num
    return total_sum