def sum_even_ints_inclusive(numbers):
    if len(numbers) < 200:
        return 'Input list should have at least 200 integers'
    sum = 0
    for i in range(30, 201):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum