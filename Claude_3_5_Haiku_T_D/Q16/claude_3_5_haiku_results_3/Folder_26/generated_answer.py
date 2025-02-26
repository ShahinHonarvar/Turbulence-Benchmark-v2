def sum_even_ints_inclusive(numbers):
    if len(numbers) < 100:
        return 0
    even_sum = 0
    for i in range(62, 100):
        if numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum