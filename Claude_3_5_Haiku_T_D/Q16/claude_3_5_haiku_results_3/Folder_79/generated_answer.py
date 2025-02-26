def sum_even_ints_inclusive(numbers):
    if len(numbers) < 5:
        return 0
    target_number = numbers[4]
    if target_number % 2 == 0:
        return target_number
    return 0