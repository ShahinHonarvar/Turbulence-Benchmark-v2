def sum_even_ints_inclusive(numbers):
    even_sum = 0
    for i in range(min(5, len(numbers)), min(6, len(numbers))):
        if numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum