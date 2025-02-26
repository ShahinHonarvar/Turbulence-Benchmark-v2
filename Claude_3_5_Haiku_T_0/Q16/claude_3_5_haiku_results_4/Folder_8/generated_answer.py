def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return 0
    target_number = numbers[23]
    return target_number if target_number % 2 == 0 else 0