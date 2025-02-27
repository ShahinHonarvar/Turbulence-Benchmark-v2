def sum_even_ints_inclusive(numbers):
    if len(numbers) < 42:
        return 0
    sum = 0
    for i in range(40, 42):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum