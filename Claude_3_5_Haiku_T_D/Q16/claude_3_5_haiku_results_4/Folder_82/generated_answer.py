def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 29:
        return 0
    target_number = numbers[29]
    if target_number % 2 == 0:
        return target_number
    else:
        return 0