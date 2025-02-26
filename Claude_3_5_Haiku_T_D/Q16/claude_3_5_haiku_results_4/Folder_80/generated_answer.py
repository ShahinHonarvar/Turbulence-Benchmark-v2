def sum_even_ints_inclusive(numbers):
    if len(numbers) < 67:
        return 0
    even_sum = 0
    for i in range(64, 67):
        if numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum