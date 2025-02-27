def sum_even_ints_inclusive(numbers):
    if len(numbers) < 93:
        return 'Input list is too short. Must have at least 93 elements.'
    sum_even = 0
    for i in range(29, 94):
        if numbers[i] % 2 == 0:
            sum_even += numbers[i]
    return sum_even