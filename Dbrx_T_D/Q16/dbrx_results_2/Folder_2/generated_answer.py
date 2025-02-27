def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(15, 40):
        if i >= 0 and i < len(numbers) and (numbers[i] % 2 == 0):
            sum += numbers[i]
    return sum