def sum_even_ints_inclusive(numbers):
    result = 0
    for i in range(min(8, len(numbers))):
        if numbers[i] % 2 == 0:
            result += numbers[i]
    return result