def sum_even_ints_inclusive(numbers):
    if len(numbers) < 86:
        return 'Input list is too short'
    sum = 0
    for i in range(43, 87):
        if i >= len(numbers):
            break
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum