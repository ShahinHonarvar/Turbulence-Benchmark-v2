def sum_even_ints_inclusive(numbers):
    even_sum = 0
    for i in range(29, 80):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum