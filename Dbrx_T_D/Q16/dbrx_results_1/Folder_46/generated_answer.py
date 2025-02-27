def sum_even_ints_inclusive(numbers):
    if len(numbers) < 88:
        return 'List is too short. Provide a list with at least 88 integers.'
    even_sum = 0
    for i in range(30, 88):
        if numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum