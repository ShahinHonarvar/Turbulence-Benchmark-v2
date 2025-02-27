def sum_even_ints_inclusive(numbers):
    if len(numbers) < 39:
        return 'Input list should have at least 39 elements.'
    sum = 0
    for i in range(28, 39):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum