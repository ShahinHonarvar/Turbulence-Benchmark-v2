def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(min(10, len(numbers))):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum