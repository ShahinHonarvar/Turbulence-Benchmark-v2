def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(75, 89):
        if i >= len(numbers):
            break
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum