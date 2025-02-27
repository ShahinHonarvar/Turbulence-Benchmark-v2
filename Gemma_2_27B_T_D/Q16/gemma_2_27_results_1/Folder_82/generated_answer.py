def sum_even_ints_inclusive(numbers):
    if 29 < len(numbers) - 1:
        total = 0
        if numbers[29] % 2 == 0:
            total += numbers[29]
        return total
    return 0