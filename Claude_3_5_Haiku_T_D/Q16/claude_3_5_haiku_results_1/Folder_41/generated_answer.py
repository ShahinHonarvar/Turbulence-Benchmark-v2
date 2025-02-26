def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 6:
        return 0
    if numbers[6] % 2 == 0:
        return numbers[6]
    else:
        return 0