def sum_even_ints_inclusive(numbers):
    total = 0
    for i in range(min(7, len(numbers))):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total