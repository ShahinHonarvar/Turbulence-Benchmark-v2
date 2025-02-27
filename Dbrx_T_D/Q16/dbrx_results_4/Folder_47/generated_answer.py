def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(min(37, len(numbers)), min(77, len(numbers))):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum