def sum_even_ints_inclusive(numbers):
    if len(numbers) < 98:
        return 'Input list is too short. Must have at least 98 elements.'
    sum = 0
    for i in range(21, 98):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum