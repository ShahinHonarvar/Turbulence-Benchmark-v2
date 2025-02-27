def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    sum = 0
    for i in range(2):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum