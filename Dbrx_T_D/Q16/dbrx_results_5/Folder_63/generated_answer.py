def sum_even_ints_inclusive(numbers):
    if not isinstance(numbers, list) or len(numbers) < 88 or len(numbers) < 22:
        return 0
    sum_even = 0
    for i in range(22, 89):
        if i < len(numbers) and numbers[i] % 2 == 0:
            sum_even += numbers[i]
    return sum_even