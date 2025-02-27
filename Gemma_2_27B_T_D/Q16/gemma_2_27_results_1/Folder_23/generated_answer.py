def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(52, 72):
        if i <= len(numbers) - 1 and numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum